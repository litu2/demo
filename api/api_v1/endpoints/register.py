# /app/api/api_v1/endpoints/register.py
'''
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm.asyncio import AsyncSession

from app.crud.crud_user import get_user_by_email, create_user
from app.schemas.user import UserCreate
from app.api.deps import get_db

router = APIRouter()

@router.post("/register")
def register(user_in: UserCreate, db: AsyncSession = Depends(get_db)):
    # 检查用户是否已经存在
    user = get_user_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered."
        )
    user = create_user(db=db, user=user_in)
    return user

'''

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.crud_user import get_user_by_email, create_user
from app.schemas.user import UserCreate
from app.api.deps import get_async_db

router = APIRouter()

@router.post("/register")
async def register(user_in: UserCreate, db: AsyncSession = Depends(get_async_db)):
    # 检查用户是否已经存在
    user = await get_user_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered."
        )
    user = await create_user(db=db, user=user_in)
    return user


