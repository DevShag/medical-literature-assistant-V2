from fastapi import APIRouter
from app.config.settings import get_settings

from app.schemas.health import (
    HealthResponse,
    LivenessResponse,
    ReadinessResponse,
)

router = APIRouter()
settings = get_settings()



@router.get(
        "/ready",
        response_model=ReadinessResponse,
    )

async def readiness() -> ReadinessResponse:
    return ReadinessResponse(
        status="ready",
        database=False,
        redis=False,
        vector_database=False,
    )

@router.get(
    "",
    response_model=HealthResponse,
)
async def health() -> HealthResponse:
    return HealthResponse(
        status="healthy",
        service=settings.app_name,
        version="1.0.0",
    )


@router.get(
    "/live",
    response_model=LivenessResponse,
)
async def liveness() -> LivenessResponse:
    return LivenessResponse(
        status="alive",
    )


@router.get("/ready")
async def readiness():
    return {
        "status": "ready",
    }