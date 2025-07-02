from typing import AsyncIterator, Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from .manager import session_manager


async def get_db_session() -> AsyncIterator[AsyncSession]:
    async with session_manager.session() as session:
        yield session


GetDBSessionDep = Annotated[AsyncSession, Depends(get_db_session)]
