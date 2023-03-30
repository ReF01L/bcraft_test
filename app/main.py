from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings

from statistics.api.v1 import router as statistic_router


def get_application():
    _app = FastAPI(title=settings.PROJECT_NAME, version='0.1.0')

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    _app.include_router(statistic_router)

    return _app


app = get_application()
