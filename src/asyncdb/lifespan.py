from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlalchemy import text

from .manager import session_manager


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        async with session_manager.session() as session:
            await session.execute(text("SELECT 1"))
        yield
    finally:
        if session_manager.is_initialized():
            await session_manager.close()
