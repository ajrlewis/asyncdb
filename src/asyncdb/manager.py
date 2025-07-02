import contextlib
from typing import Any, AsyncIterator, Optional

from loguru import logger
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_session_maker,
    create_async_engine,
)

from .config import settings  # Assume settings is passed or imported from the app


class DatabaseSessionManager:
    def __init__(self, host: str, engine_kwargs: Optional[dict[str, Any]] = None):
        engine_kwargs = engine_kwargs or {}
        logger.debug("[DB] Initializing engine...")
        self._engine: Optional[AsyncEngine] = create_async_engine(host, **engine_kwargs)
        self._session_maker = async_session_maker(
            autocommit=False,
            autoflush=False,
            bind=self._engine,
        )

    async def close(self) -> None:
        if not self._engine:
            raise RuntimeError("Engine not initialized")
        logger.debug("[DB] Disposing engine...")
        await self._engine.dispose()
        self._engine = None
        self._session_maker = None

    @contextlib.asynccontextmanager
    async def session(self) -> AsyncIterator[AsyncSession]:
        if not self._session_maker:
            raise RuntimeError("Session maker not initialized")
        session = self._session_maker()
        try:
            yield session
        except Exception as e:
            await session.rollback()
            raise e
        finally:
            await session.close()

    def is_initialized(self) -> bool:
        return self._engine is not None

    @classmethod
    def from_settings(cls):
        return cls(settings.SQLALCHEMY_DATABASE_URI, {"echo": True})


session_manager = DatabaseSessionManager.from_settings()
