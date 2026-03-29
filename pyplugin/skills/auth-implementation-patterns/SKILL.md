---
name: auth-implementation-patterns
description: "Build secure, scalable authentication and authorization systems using industry-standard patterns and modern best practices."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Authentication & Authorization Implementation Patterns

Build secure, scalable authentication and authorization systems using industry-standard patterns and modern best practices.

## Use this skill when

- Implementing user authentication systems
- Securing REST or GraphQL APIs
- Adding OAuth2/social login or SSO
- Designing session management or RBAC
- Debugging authentication or authorization issues

## Do not use this skill when

- You only need UI copy or login page styling
- The task is infrastructure-only without identity concerns
- You cannot change auth policies or credential storage

## Instructions

- Define users, tenants, flows, and threat model constraints.
- Choose auth strategy (session, JWT, OIDC) and token lifecycle.
- Design authorization model and policy enforcement points.
- Plan secrets storage, rotation, logging, and audit requirements.
- If detailed examples are required, open `resources/implementation-playbook.md`.

## Safety

- Never log secrets, tokens, or credentials.
- Enforce least privilege and secure storage for keys.

## Common Implementation Patterns

### JWT Token Pattern

```python
from fastapi import Depends, HTTPException
from jose import JWTError, jwt
from pydantic import BaseModel
from datetime import datetime, timedelta
from typing import Optional

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"

class TokenPayload(BaseModel):
    sub: str  # user ID
    exp: int  # expiration time
    role: str

def create_access_token(user_id: str, role: str, expires_delta: Optional[timedelta] = None) -> str:
    """Create JWT token with user info"""
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(hours=1)

    payload = {
        "sub": user_id,
        "role": role,
        "exp": int(expire.timestamp())
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

async def get_current_user(token: str = Depends(oauth2_scheme)) -> TokenPayload:
    """Dependency: extract and validate JWT token"""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return TokenPayload(**payload)
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

@app.post("/login")
async def login(username: str, password: str) -> dict:
    """Login endpoint that returns JWT"""
    user = verify_credentials(username, password)
    token = create_access_token(user.id, user.role)
    return {"access_token": token, "token_type": "bearer"}
```

### Session Token Pattern

```python
from fastapi import Cookie, Response, HTTPException
from fastapi.responses import JSONResponse
import secrets

# Session storage (use Redis in production)
sessions: dict[str, dict] = {}

def create_session(user_id: str, role: str) -> str:
    """Create session token and store session data"""
    session_token = secrets.token_urlsafe(32)
    sessions[session_token] = {
        "user_id": user_id,
        "role": role,
        "created_at": datetime.utcnow()
    }
    return session_token

@app.post("/login")
async def login(username: str, password: str) -> JSONResponse:
    """Login endpoint that sets session cookie"""
    user = verify_credentials(username, password)
    session_token = create_session(user.id, user.role)

    response = JSONResponse({"status": "ok"})
    response.set_cookie(
        "session_id",
        session_token,
        httponly=True,      # Prevent JavaScript access
        secure=True,        # HTTPS only
        samesite="strict"   # CSRF protection
    )
    return response

async def get_session(session_id: str = Cookie(None)) -> dict:
    """Dependency: retrieve and validate session"""
    if not session_id or session_id not in sessions:
        raise HTTPException(status_code=401, detail="Invalid session")
    return sessions[session_id]

@app.get("/me")
async def get_user(session: dict = Depends(get_session)) -> dict:
    """Protected endpoint using session"""
    return {"user_id": session["user_id"], "role": session["role"]}
```

### Role-Based Access Control (RBAC) Pattern

```python
from enum import StrEnum
from typing import Callable

class Role(StrEnum):
    ADMIN = "admin"
    USER = "user"
    VIEWER = "viewer"

def require_role(required_role: Role) -> Callable:
    """Dependency factory for role-based access control"""
    async def check_role(user: TokenPayload = Depends(get_current_user)) -> TokenPayload:
        if user.role != required_role.value:
            raise HTTPException(status_code=403, detail="Insufficient permissions")
        return user
    return Depends(check_role)

@app.delete("/users/{user_id}")
async def delete_user(user_id: str, admin: TokenPayload = require_role(Role.ADMIN)):
    """Only admins can delete users"""
    # Implementation
    pass

@app.get("/admin/dashboard")
async def admin_dashboard(admin: TokenPayload = require_role(Role.ADMIN)):
    """Admin-only endpoint"""
    return {"dashboard": "admin data"}
```

## Keywords That Should Trigger This Skill

- "JWT", "token", "OAuth2", "OpenID Connect"
- "session", "cookie", "authentication"
- "RBAC", "role", "permission", "authorization"
- "access control", "token refresh"

## Resources

- `resources/implementation-playbook.md` for advanced patterns and multi-tenant scenarios.
