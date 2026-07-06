from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: str
    service: str
    version: str


class LivenessResponse(BaseModel):
    status: str


class ReadinessResponse(BaseModel):
    status: str
    database: bool
    redis: bool
    vector_database: bool