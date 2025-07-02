# asyncdb

**asyncdb** is a lightweight and reusable asynchronous database session manager for Python applications using **SQLAlchemy** and **FastAPI**. It provides a consistent and maintainable way to manage async DB sessions, dependencies, and app lifecycle setup across multiple services.

## 🚀 Features

- Asynchronous SQLAlchemy engine and session management
- FastAPI-compatible dependency injection
- Centralized database lifecycle control (`lifespan`)
- Declarative base for ORM models
- Easily reusable across multiple projects

## 📦 Installation

Install via local path (during development):

```bash
pip install -e ./asyncdb
```

## 🧰 Usage

1. Register Lifespan in FastAPI

```python
from fastapi import FastAPI
from asyncdb import lifespan

app = FastAPI(lifespan=lifespan)
```

2. Use DB Session Dependency in Routes

```python
from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from asyncdb import GetDBSessionDep

router = APIRouter()

@router.get("/users/")
async def list_users(db: GetDBSessionDep):
    result = await db.execute(...)
    return result.scalars().all()
```

3. Define Models Using Base

```python
from sqlalchemy import Column, Integer, String
from asyncdb import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String)
```

4. Configure Settings (Optional)

Ensure your project provides a settings object with SQLALCHEMY_DATABASE_URI. Example:

```python
# config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URI: str = "sqlite+aiosqlite:///./test.db"

settings = Settings()
```

## 📁 Module Overview

| Module          | Description                                     |
|-----------------|-------------------------------------------------|
| manager.py      | Core DatabaseSessionManager class               |
| dependencies.py | FastAPI-compatible session dependency injection |
| lifespan.py     | Lifespan context for DB connection lifecycle    |
| base.py         | Declarative base for SQLAlchemy ORM             |

## ✅ Requirements

- Python 3.10+
- SQLAlchemy 2.x
- FastAPI
- Loguru

Install dependencies via:

```bash
pip install -r requirements.txt
```

## 🧪 Example Projects

Coming soon — feel free to contribute a working example repo using asyncdb!

## 📄 License

MIT License © AJRLewis

## 🤝 Contributing

Contributions welcome! Open an issue or submit a PR for enhancements, bug fixes, or docs.
