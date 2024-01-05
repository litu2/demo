
'''
from typing import Generator
from app.db.session import SessionLocal


# 依赖项用于获取数据库会话
def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
'''



from typing import AsyncGenerator
from app.db.session import async_session

# 依赖项用于获取数据库会话
async def get_async_db() -> AsyncGenerator:
    async with async_session() as session:
        yield session
