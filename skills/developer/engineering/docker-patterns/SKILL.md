---
name: docker-patterns
description: 面向本地开发、加固的 CLI 安装器 harness、容器安全、网络、卷与多服务编排的 Docker 与 Docker Compose 模式。适用于编写或审查 Dockerfile 与 Compose 服务、跨 Linux 发行版测试安装器，或规划准确的 macOS 与 Windows 原生验证。
---

> **中文汉化版** · 上游：[affaan-m/ECC](https://github.com/affaan-m/ECC) · 原文件：`skills/docker-patterns/SKILL.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Docker 模式

容器化开发的 Docker 与 Docker Compose 最佳实践。

## 用 Docker Compose 做本地开发

### 标准 Web 应用栈

```yaml
# docker-compose.yml
services:
  app:
    build:
      context: .
      target: dev                     # Use dev stage of multi-stage Dockerfile
    ports:
      - "3000:3000"
    volumes:
      - .:/app                        # Bind mount for hot reload
      - /app/node_modules             # Anonymous volume -- preserves container deps
    environment:
      - DATABASE_URL=postgres://postgres:postgres@db:5432/app_dev
      - REDIS_URL=redis://redis:6379/0
      - NODE_ENV=development
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_started
    command: npm run dev

  db:
    image: postgres:16-alpine
    ports:
      - "5432:5432"
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
      POSTGRES_DB: app_dev
    volumes:
      - pgdata:/var/lib/postgresql/data
      - ./scripts/init-db.sql:/docker-entrypoint-initdb.d/init.sql
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 5s
      timeout: 3s
      retries: 5

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    volumes:
      - redisdata:/data

  mailpit:                            # Local email testing
    image: axllent/mailpit
    ports:
      - "8025:8025"                   # Web UI
      - "1025:1025"                   # SMTP

volumes:
  pgdata:
  redisdata:
```

### 开发与生产 Dockerfile

```dockerfile
# Stage: dependencies
FROM node:22-alpine AS deps
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci

# Stage: dev (hot reload, debug tools)
FROM node:22-alpine AS dev
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY . .
EXPOSE 3000
CMD ["npm", "run", "dev"]

# Stage: build
FROM node:22-alpine AS build
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY . .
RUN npm run build && npm prune --production

# Stage: production (minimal image)
FROM node:22-alpine AS production
WORKDIR /app
RUN addgroup -g 1001 -S appgroup && adduser -S appuser -u 1001
USER appuser
COPY --from=build --chown=appuser:appgroup /app/dist ./dist
COPY --from=build --chown=appuser:appgroup /app/node_modules ./node_modules
COPY --from=build --chown=appuser:appgroup /app/package.json ./
ENV NODE_ENV=production
EXPOSE 3000
HEALTHCHECK --interval=30s --timeout=3s CMD wget -qO- http://localhost:3000/health || exit 1
CMD ["node", "dist/server.js"]
```

### Override 文件

```yaml
# docker-compose.override.yml (auto-loaded, dev-only settings)
services:
  app:
    environment:
      - DEBUG=app:*
      - LOG_LEVEL=debug
    ports:
      - "9229:9229"                   # Node.js debugger

# docker-compose.prod.yml (explicit for production)
services:
  app:
    build:
      target: production
    restart: always
    deploy:
      resources:
        limits:
          cpus: "1.0"
          memory: 512M
```

```bash
# Development (auto-loads override)
docker compose up

# Production
docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d
```

## 网络

### 服务发现

同一 Compose 网络内的服务可以通过服务名互相解析：
```
# From "app" container:
postgres://postgres:postgres@db:5432/app_dev    # "db" resolves to the db container
redis://redis:6379/0                             # "redis" resolves to the redis container
```

### 自定义网络

```yaml
services:
  frontend:
    networks:
      - frontend-net

  api:
    networks:
      - frontend-net
      - backend-net

  db:
    networks:
      - backend-net              # Only reachable from api, not frontend

networks:
  frontend-net:
  backend-net:
```

### 只暴露必要的端口

```yaml
services:
  db:
    ports:
      - "127.0.0.1:5432:5432"   # Only accessible from host, not network
    # Omit ports entirely in production -- accessible only within Docker network
```

## 卷策略

```yaml
volumes:
  # Named volume: persists across container restarts, managed by Docker
  pgdata:

  # Bind mount: maps host directory into container (for development)
  # - ./src:/app/src

  # Anonymous volume: preserves container-generated content from bind mount override
  # - /app/node_modules
```

### 常见模式

```yaml
services:
  app:
    volumes:
      - .:/app                   # Source code (bind mount for hot reload)
      - /app/node_modules        # Protect container's node_modules from host
      - /app/.next               # Protect build cache

  db:
    volumes:
      - pgdata:/var/lib/postgresql/data          # Persistent data
      - ./scripts/init.sql:/docker-entrypoint-initdb.d/init.sql  # Init scripts
```

## 容器安全

### Dockerfile 加固

```dockerfile
# 1. Use specific tags (never :latest)
FROM node:22.12-alpine3.20

# 2. Run as non-root
RUN addgroup -g 1001 -S app && adduser -S app -u 1001
USER app

# 3. Drop capabilities (in compose)
# 4. Read-only root filesystem where possible
# 5. No secrets in image layers
```

### Compose 安全

```yaml
services:
  app:
    security_opt:
      - no-new-privileges:true
    read_only: true
    tmpfs:
      - /tmp
      - /app/.cache
    cap_drop:
      - ALL
    cap_add:
      - NET_BIND_SERVICE          # Only if binding to ports < 1024
```

### 密钥管理

```yaml
# GOOD: Use environment variables (injected at runtime)
services:
  app:
    env_file:
      - .env                     # Never commit .env to git
    environment:
      - API_KEY                  # Inherits from host environment

# GOOD: Docker secrets (Swarm mode)
secrets:
  db_password:
    file: ./secrets/db_password.txt

services:
  db:
    secrets:
      - db_password

# BAD: Hardcoded in image
# ENV API_KEY=sk-proj-xxxxx      # NEVER DO THIS
```

## 加固的 CLI 安装器 Harness

用容器针对一次性项目副本测试安装器行为，且不允许测试改动源码检出。

### 尊重平台边界

- 针对 Debian、Ubuntu 等 Linux 发行版，运行真实容器。
- macOS 无法作为 Docker 容器运行，因为 Docker 共享的是 Linux 内核。同一套无 shell 的测试入口要在 macOS 上原生运行。
- Windows 容器需要 Windows Docker 引擎。平台无关的逻辑放到原生 Windows CI runner 上运行，Windows 容器留给 Windows 宿主机。
- 保留原生的 Ubuntu/macOS/Windows CI 矩阵，覆盖宿主机特有的路径、命令 shim、引号处理和文件系统行为。

不要声称 Linux 容器可以验证 macOS 或 Windows 的行为。

### 强制执行隔离契约

- 用不可变 digest 固定基础镜像，并固定所安装的 CLI 版本。
- 发行版账户名不一致时，以非 root 的数字 UID/GID 运行。
- 以只读方式挂载本仓库与源项目。
- 任何改动之前，先把源项目复制进可写的 `tmpfs` 工作区。
- 挂载 `/workspace` 时使用 `noexec`、UID/GID 1000 和 `mode=0700`，
  只有容器用户能查看项目数据。
- 把 npm 与 npx 的可执行缓存放在可执行的 `/tmp` 挂载上的
  `NPM_CONFIG_CACHE=/tmp/npm-cache`。默认大小为 2 GiB，可用
  `ECC_TMPFS_SIZE` 调整；`ECC_WORKSPACE_SIZE` 则单独控制私有
  工作区挂载的大小。
- 设置 `read_only: true`、`no-new-privileges:true`、`cap_drop: [ALL]` 和有限的 `pids_limit`。
- 默认的 real-CLI 服务保持 `network_mode: none`。需要网络访问时，
  只通过一个命名清晰、需显式选择加入的服务提供，用于需要认证的
  provider 会话；绝不让它成为环境变量驱动的隐性默认。
- 只创建工具所需的可写临时路径。
- 默认不把宿主机凭证传入容器。
- 默认执行 dry run，白名单只包含显式的 `dry-run`、`install`、
  `plugin` 和 `shell` 模式。
- 跨平台 runner 使用参数数组或 `spawnSync(..., { shell: false })`。绝不把项目路径插值进 shell 命令。

### 演练 ECC Plugin Setup Harness

以 `docker/plugin-setup/compose.yaml` 作为参考实现。它提供：

- `fixture-tests`：聚焦的安装 manifest、target 与 executor 测试套件。
- `real-cli`：版本固定的基于 Debian 的通用 Linux 镜像。
- `real-cli-ubuntu`：版本固定的 Ubuntu 镜像。

构建前先校验 Compose 模型：

```bash
docker compose -f docker/plugin-setup/compose.yaml config --quiet
```

构建两个真实 Linux 镜像：

```bash
docker compose -f docker/plugin-setup/compose.yaml \
  build real-cli real-cli-ubuntu
```

在每个镜像中运行安全的默认流程：

```bash
docker compose -p ecc-plugin-debian-test \
  -f docker/plugin-setup/compose.yaml \
  run --rm -T real-cli dry-run

docker compose -p ecc-plugin-ubuntu-test \
  -f docker/plugin-setup/compose.yaml \
  run --rm -T real-cli-ubuntu dry-run
```

dry run 执行的是当前公开的命令契约：

```bash
ecc install --profile core --target claude-project --dry-run --json
```

在该命令运行之前，容器会先从只读检出（checkout）中用
`npm pack --ignore-scripts` 打出本地 npm 产物。它把自建的 tarball 解压到
`/tmp` 下，校验 `ecc-universal` 包名、必需的安装 manifest，
以及受限的 `package.json` `bin.ecc` 映射，然后调用解压出来的
`ecc` 可执行文件。运行时保持在
`network_mode: none`，不执行包生命周期脚本，
也不依赖宿主机的 `node_modules`；其精确固定的生产依赖
已经包含在镜像里。

harness 会拒绝空计划、非 `claude-project` 的 target、
`/workspace/project/.claude` 之外的任何操作，以及会创建目标目录的 dry run。
`install` 会执行两次隔离的 apply，检查其托管的安装状态，
列出已安装的 target，并运行 `doctor`。

### 启动、打开、重连并清理命名会话

启动 detached 容器时不要带 `--rm`，这样退出终端也不会移除
该会话：

```bash
docker compose -p ecc-plugin-session \
  -f docker/plugin-setup/compose.yaml \
  run --detach --name ecc-plugin-shell real-cli shell
```

容器会把只读 fixture 复制到稳定的私有目录
`/workspace/project`。确认容器在运行，然后产出 terminal-opener v1
数据契约的 Docker 侧：

```bash
docker inspect --format '{{.State.Running}}' ecc-plugin-shell
node docker/plugin-setup/interactive-plan.js \
  --container ecc-plugin-shell \
  --workdir /workspace/project \
  --json \
  -- bash
```

JSON 结果的边界恰好只有 `executable` 和 `argv` 两项（外加
`contractVersion: 1`）：可执行文件是 `docker`，argv 以
`exec`、`-it`、`-w` 开头。装好独立的 terminal-opener skill 后，
把这份数据传给它。这个 Docker harness 刻意不导入终端适配器，
不拼接 shell 命令，也不管理宿主机 GUI 进程。
在那之前，直接在当前宿主机终端打开同一个 PTY：

```bash
docker exec -it -w /workspace/project ecc-plugin-shell bash
```

退出 shell 时不要停止 detached 容器。用同一条 `docker exec -it`
命令重连。结束后，精确删除这个命名容器
及其 Compose 项目资源：

```bash
docker rm --force ecc-plugin-shell
docker compose -p ecc-plugin-session \
  -f docker/plugin-setup/compose.yaml \
  down --remove-orphans
```

默认不传入宿主机凭证，凭证目录也从不挂载。默认服务同样没有网络。
当需要认证的 provider 会话确实需要网络时，先构建 `real-cli`，
然后以显式可见的方式选择加入：
`docker compose -f docker/plugin-setup/compose.yaml
--profile networked run --service-ports real-cli-networked shell`。
`--service-ports` 标志会发布该服务的 loopback 回调映射。
优先在这个一次性会话内完成认证。如果某次 CI 运行必须
继承宿主机环境变量中的凭证，就在调用时以显式的 Compose
`--env NAME` 标志选择加入，并明确接受该值在容器存活期内
可被查看、可被外带这一事实，然后立即
精确删除这个命名容器。

### 在联网会话内完成 Codex 认证

`codex login` 会把它的 OAuth 回调服务器绑定到容器内的
`127.0.0.1:1455`。Docker 端口发布转发到的是容器网络接口而非
loopback，所以宿主机浏览器重定向到 `http://localhost:1455` 时，
没有桥接就会被拒绝。`real-cli-networked` 服务把宿主机
`127.0.0.1:1455` 发布到容器端口 `1456`；登录前先把该端口
桥接回 loopback：

```bash
(
  set -e
  npm install --global @openai/codex@0.162.0   # the harness image does not ship codex
  node /ecc/docker/plugin-setup/codex-auth-relay.js &
  relay_pid=$!
  trap 'kill "$relay_pid" 2>/dev/null || true; wait "$relay_pid" 2>/dev/null || true' EXIT
  codex login
)
```

联网服务会设置 `NPM_CONFIG_PREFIX=/tmp/ecc-npm` 并把其 `bin`
目录加入 `PATH`。这样，在可执行的 `/tmp` 挂载上，UID 1000 对固定版本
的安装仍可写，同时根文件系统保持只读。

在宿主机浏览器里完成登录。每次尝试都会生成新的
`state`/`code`，所以始终跟随最新打印出的链接。token 保存在
一次性容器的 `~/.codex/auth.json` 里；删除命名容器
即删除这份凭证副本。登录代码块无论成败都会停掉 relay。
同一时刻只能有一个容器占用宿主机端口 1455，
因为 OAuth 重定向指向固定端口。

宿主机侧的发布仅限 loopback。容器内，relay 监听所有接口，
Docker 才能转发到它；运行期间，同一 bridge 网络上的其他容器
也能访问它。这次登录要使用没有不受信对端的专用网络，
用完立即精确删除命名容器。
空闲的回调连接会在 30 秒后关闭。

在宿主机上原生运行同一套聚焦测试套件：

```bash
npm run test:plugin-setup-platform
```

在信任镜像之前，先检查它构建出的身份与环境：

```bash
docker image inspect ecc-plugin-setup:debian ecc-plugin-setup:ubuntu
```

清理每个命名测试项目，且不误删无关的卷或镜像：

```bash
docker compose -p ecc-plugin-debian-test \
  -f docker/plugin-setup/compose.yaml down --remove-orphans
docker compose -p ecc-plugin-ubuntu-test \
  -f docker/plugin-setup/compose.yaml down --remove-orphans
```

## .dockerignore

```
node_modules
.git
.env
.env.*
dist
coverage
*.log
.next
.cache
docker-compose*.yml
Dockerfile*
README.md
tests/
```

## 调试

### 常用命令

```bash
# View logs
docker compose logs -f app           # Follow app logs
docker compose logs --tail=50 db     # Last 50 lines from db

# Execute commands in running container
docker compose exec app sh           # Shell into app
docker compose exec db psql -U postgres  # Connect to postgres

# Inspect
docker compose ps                     # Running services
docker compose top                    # Processes in each container
docker stats                          # Resource usage

# Rebuild
docker compose up --build             # Rebuild images
docker compose build --no-cache app   # Force full rebuild

# Clean up
docker compose down                   # Stop and remove containers
docker compose down -v                # Also remove volumes (DESTRUCTIVE)
docker system prune                   # Remove unused images/containers
```

### 排查网络问题

```bash
# Check DNS resolution inside container
docker compose exec app nslookup db

# Check connectivity
docker compose exec app wget -qO- http://api:3000/health

# Inspect network
docker network ls
docker network inspect <project>_default
```

## 反模式

```
# BAD: Using docker compose in production without orchestration
# Use Kubernetes, ECS, or Docker Swarm for production multi-container workloads

# BAD: Storing data in containers without volumes
# Containers are ephemeral -- all data lost on restart without volumes

# BAD: Running as root
# Always create and use a non-root user

# BAD: Using :latest tag
# Pin to specific versions for reproducible builds

# BAD: One giant container with all services
# Separate concerns: one process per container

# BAD: Putting secrets in docker-compose.yml
# Use .env files (gitignored) or Docker secrets
```
