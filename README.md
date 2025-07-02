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
