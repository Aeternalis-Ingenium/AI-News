from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import run

from src.api.endpoints import router as api_endpoint_router
from src.config.settings.settings import Settings
from src.config.setup import settings


def initialize_application(settings: Settings = settings) -> FastAPI:
    app = FastAPI(**settings.set_backend_app_attributes)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_ORIGINS,
        allow_credentials=settings.IS_ALLOWED_CREDENTIALS,
        allow_methods=settings.ALLOWED_METHODS,
        allow_headers=settings.ALLOWED_HEADERS,
    )
    app.include_router(router=api_endpoint_router, prefix=settings.API_PREFIX)
    return app


app: FastAPI = initialize_application()

if __name__ == "__main__":
    run(
        app="main:app",
        host=settings.SERVER_HOST,
        port=settings.SERVER_PORT,
        reload=settings.DEBUG,
        workers=settings.SERVER_WORKERS,
        log_level=settings.LOGGING_LEVEL,
    )
