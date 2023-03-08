from fastapi import APIRouter

from src.api.routes.auth import router as auth_router

router = APIRouter(
    prefix="/v1",
)
router.include_router(router=auth_router)
