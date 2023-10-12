from fastapi import APIRouter, Depends

from app.auth.models import User
from app.auth.schemas import UserCreate, UserRead
from app.auth.base_config import auth_backend, fastapi_users


router = APIRouter(
    prefix = '/auth',
    tags = ['auth']
)


router.include_router(
    fastapi_users.get_auth_router(auth_backend),
)

router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
)

current_user = fastapi_users.current_user()

@router.get("/authenticated-route")
async def authenticated_route(user: User = Depends(current_user)):
    return {"message": f"Hello {user.email}!"}