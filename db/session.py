#from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine


DATABASE_URL = "mysql+aiomysql://work:work2023@localhost/dbxu"


# 创建异步数据库引擎
engine = create_async_engine(DATABASE_URL,echo=True)

# 使用基于类的自定义 sessionmaker：
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


'''
# 创建数据库引擎
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# 创建会话工厂
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

'''
