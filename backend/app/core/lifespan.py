from contextlib import asynccontextmanager

from fastapi import FastAPI

import structlog

logger = structlog.get_logger()


@asynccontextmanager
async def lifespan(app: FastAPI):

    logger.info("application_starting")

    yield

    logger.info("application_stopping")