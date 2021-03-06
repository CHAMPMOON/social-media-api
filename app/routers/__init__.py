from fastapi import APIRouter

from .post import router as post_router
from .user import router as user_router
from .auth import router as auth_router
from .vote import router as vote_router


router = APIRouter()
router.include_router(post_router)
router.include_router(user_router)
router.include_router(auth_router)
router.include_router(vote_router)
