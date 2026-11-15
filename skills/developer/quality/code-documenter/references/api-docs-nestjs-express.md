> **中文汉化版** · 上游：[Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) · 原文件：`skills/developer/quality/code-documenter/references/api-docs-nestjs-express.md` · License: MIT
> 翻译日期：2026-11-15 · 同步状态：上游 HEAD（2026-11-15 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# API 文档：NestJS 与 Express

## NestJS（@nestjs/swagger）

NestJS 需要显式装饰器来生成 OpenAPI 文档。

### Controller 文档

```typescript
import { Controller, Post, Body, Get, Param } from '@nestjs/common';
import {
  ApiTags,
  ApiOperation,
  ApiResponse,
  ApiParam,
  ApiBearerAuth,
} from '@nestjs/swagger';

@ApiTags('Users')
@ApiBearerAuth()
@Controller('users')
export class UsersController {
  @Post()
  @ApiOperation({ summary: 'Create a new user' })
  @ApiResponse({
    status: 201,
    description: 'User created successfully',
    type: UserDto,
  })
  @ApiResponse({
    status: 400,
    description: 'Invalid input data',
  })
  async create(@Body() dto: CreateUserDto): Promise<UserDto> {
    return this.usersService.create(dto);
  }

  @Get(':id')
  @ApiOperation({ summary: 'Get user by ID' })
  @ApiParam({
    name: 'id',
    description: 'User unique identifier',
    example: '123',
  })
  @ApiResponse({ status: 200, type: UserDto })
  @ApiResponse({ status: 404, description: 'User not found' })
  async findOne(@Param('id') id: string): Promise<UserDto> {
    return this.usersService.findOne(id);
  }
}
```

### DTO 文档

```typescript
import { ApiProperty, ApiPropertyOptional } from '@nestjs/swagger';
import { IsEmail, IsString, MinLength } from 'class-validator';

export class CreateUserDto {
  @ApiProperty({
    description: "User's display name",
    example: 'John Doe',
    minLength: 1,
    maxLength: 100,
  })
  @IsString()
  @MinLength(1)
  name: string;

  @ApiProperty({
    description: "User's email address",
    example: 'john@example.com',
  })
  @IsEmail()
  email: string;

  @ApiPropertyOptional({
    description: 'Profile picture URL',
    example: 'https://example.com/avatar.jpg',
  })
  avatarUrl?: string;
}
```

## Express（swagger-jsdoc）

Express 使用带 swagger 注解的 JSDoc 注释。

### 配置

```javascript
const swaggerJsdoc = require('swagger-jsdoc');
const swaggerUi = require('swagger-ui-express');

const options = {
  definition: {
    openapi: '3.0.0',
    info: {
      title: 'API Documentation',
      version: '1.0.0',
    },
  },
  apis: ['./routes/*.js'],
};

const specs = swaggerJsdoc(options);
app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(specs));
```

### 路由文档

```javascript
/**
 * @swagger
 * /users:
 *   post:
 *     summary: Create a new user
 *     tags: [Users]
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             $ref: '#/components/schemas/CreateUser'
 *     responses:
 *       201:
 *         description: User created successfully
 *         content:
 *           application/json:
 *             schema:
 *               $ref: '#/components/schemas/User'
 *       400:
 *         description: Invalid input
 */
router.post('/users', createUser);

/**
 * @swagger
 * /users/{id}:
 *   get:
 *     summary: Get user by ID
 *     tags: [Users]
 *     parameters:
 *       - in: path
 *         name: id
 *         required: true
 *         schema:
 *           type: string
 *         description: User ID
 *     responses:
 *       200:
 *         description: User found
 *         content:
 *           application/json:
 *             schema:
 *               $ref: '#/components/schemas/User'
 *       404:
 *         description: User not found
 */
router.get('/users/:id', getUser);
```

### Schema 文档

```javascript
/**
 * @swagger
 * components:
 *   schemas:
 *     CreateUser:
 *       type: object
 *       required:
 *         - name
 *         - email
 *       properties:
 *         name:
 *           type: string
 *           description: User's display name
 *           example: John Doe
 *         email:
 *           type: string
 *           format: email
 *           description: User's email address
 *           example: john@example.com
 *     User:
 *       allOf:
 *         - $ref: '#/components/schemas/CreateUser'
 *         - type: object
 *           properties:
 *             id:
 *               type: string
 *               description: Unique identifier
 *             createdAt:
 *               type: string
 *               format: date-time
 */
```

## 速查表

| NestJS 装饰器 | 用途 |
|------------------|---------|
| `@ApiTags()` | 给端点分组 |
| `@ApiOperation()` | 端点摘要 |
| `@ApiResponse()` | 响应文档 |
| `@ApiParam()` | 路径参数 |
| `@ApiQuery()` | 查询参数 |
| `@ApiBody()` | 请求体 |
| `@ApiBearerAuth()` | 认证要求 |
| `@ApiProperty()` | DTO 属性 |

| Express swagger-jsdoc | 用途 |
|-----------------------|---------|
| `@swagger` | 起始 swagger 块 |
| `tags` | 给端点分组 |
| `summary` | 简述 |
| `parameters` | 路径/查询参数 |
| `requestBody` | 请求体 schema |
| `responses` | 响应 schema |
| `$ref` | 引用 schema |
