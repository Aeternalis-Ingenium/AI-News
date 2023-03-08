from decouple import config

from src.config.settings.environment import Environment
from src.config.settings.settings import Settings


class StagingSettings(Settings):
    VERSION: str = config("API_VERSION", cast=str)  # type: ignore
    DESCRIPTION: str | None = f"[Test Settings] Backend Application {VERSION} with FastAPI, MongoDB Atlas, and Docker."
    DEBUG = config("IS_DEBUG", cast=bool)  # type: ignore
    ENVIRONMENT: Environment = Environment.TEST
