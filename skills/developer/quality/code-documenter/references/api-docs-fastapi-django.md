> **中文汉化版** · 上游：[Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) · 原文件：`skills/developer/quality/code-documenter/references/api-docs-fastapi-django.md` · License: MIT
> 翻译日期：2026-11-15 · 同步状态：上游 HEAD（2026-11-15 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# API 文档：FastAPI 与 Django

## FastAPI（从类型自动生成）

FastAPI 从类型注解和 docstring 自动生成 OpenAPI 文档。

### 端点文档

```python
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

class UserCreate(BaseModel):
    """User creation request body."""

    name: str = Field(..., min_length=1, max_length=100, example="John Doe")
    email: str = Field(..., example="john@example.com")

class UserResponse(BaseModel):
    """User response with generated ID."""

    id: int = Field(..., example=1)
    name: str
    email: str

@app.post(
    "/users",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new user",
    tags=["Users"],
)
async def create_user(user: UserCreate) -> UserResponse:
    """Create a new user account.

    Args:
        user: User creation data including name and email.

    Returns:
        Created user with generated ID.

    Raises:
        HTTPException: 400 if email already exists.
    """
```

### 带标签的路由

```python
from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["Users"],
    responses={404: {"description": "Not found"}},
)

@router.get(
    "/{user_id}",
    response_model=UserResponse,
    summary="Get user by ID",
)
async def get_user(user_id: int) -> UserResponse:
    """Retrieve a user by their unique identifier."""
```

## Django REST Framework（drf-spectacular）

### ViewSet 文档

```python
from rest_framework import viewsets, status
from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema, OpenApiParameter

class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing user accounts.

    list: Get all users with pagination.
    create: Create a new user account.
    retrieve: Get a specific user by ID.
    update: Update all user fields.
    partial_update: Update specific user fields.
    destroy: Delete a user account.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    @extend_schema(
        summary="Get current user",
        description="Returns the authenticated user's profile",
        responses={200: UserSerializer},
    )
    @action(detail=False, methods=["get"])
    def me(self, request):
        """Get the authenticated user's profile."""
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)
```

### Serializer 文档

```python
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    """Serializer for user model with validation."""

    class Meta:
        model = User
        fields = ["id", "name", "email", "created_at"]
        read_only_fields = ["id", "created_at"]

    name = serializers.CharField(
        help_text="User's display name",
        max_length=100,
    )
    email = serializers.EmailField(
        help_text="User's email address (unique)",
    )
```

### 自定义 Schema

```python
from drf_spectacular.utils import extend_schema, OpenApiExample

@extend_schema(
    request=UserCreateSerializer,
    responses={
        201: UserSerializer,
        400: OpenApiTypes.OBJECT,
    },
    examples=[
        OpenApiExample(
            "Valid request",
            value={"name": "John", "email": "john@example.com"},
        ),
    ],
)
def create(self, request):
    """Create a new user."""
```

## 速查表

| 框架 | 文档来源 | 输出 |
|-----------|---------------------|--------|
| FastAPI | 类型注解 + docstring | 自动生成 Swagger UI |
| DRF | Serializer + drf-spectacular | 自动生成 Swagger UI |

| FastAPI 装饰器 | 用途 |
|-------------------|---------|
| `summary` | 端点简述 |
| `description` | 详细描述 |
| `tags` | 给端点分组 |
| `response_model` | 响应 schema |
| `responses` | 补充响应状态码 |

| DRF 装饰器 | 用途 |
|---------------|---------|
| `@extend_schema` | 自定义 schema |
| `OpenApiParameter` | 查询/路径参数 |
| `OpenApiExample` | 请求示例 |
