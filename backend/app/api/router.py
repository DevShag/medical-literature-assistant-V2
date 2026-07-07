from fastapi import APIRouter

from app.api.v1.health import router as health_router
from app.config.constants import HEALTH_PREFIX

api_router = APIRouter()

api_router.include_router(
    health_router,
    prefix=HEALTH_PREFIX,
    tags=["Health"],
)
