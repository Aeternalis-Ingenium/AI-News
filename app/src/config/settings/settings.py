import logging
from pathlib import Path

from decouple import config
from pydantic import BaseConfig, BaseSettings, SecretStr


class Settings(BaseSettings):
    TITLE: str = "AI News"
    VERSION: str = config("API_VERSION", cast=str)  # type: ignore
    TIMEZONE: str = "UTC"
    DESCRIPTION: str | None = (
        f"[Production Settings] Backend Application {VERSION} with FastAPI, MongoDB Atlas, and Docker."
    )
    DEBUG: bool = False

    SERVER_HOST: str = config("BACKEND_SERVER_HOST", cast=str)  # type: ignore
    SERVER_PORT: int = config("BACKEND_SERVER_PORT", cast=int)  # type: ignore
    SERVER_WORKERS: int = config("BACKEND_SERVER_WORKERS", cast=int)  # type: ignore
    API_PREFIX: str = "/api"
    CLIENT_PREFIX = ""
    DOCS_URL: str = "/docs"
    OPENAPI_URL: str = "/openapi.json"
    REDOC_URL: str = "/redoc"
    OPENAPI_PREFIX: str = ""

    JWT_TOKEN_PREFIX: str = config("JWT_TOKEN_PREFIX", cast=str)  # type: ignore
    JWT_PUBLIC_KEY: SecretStr = SecretStr(config("JWT_PUBLIC_KEY", cast=str))  # type: ignore
    JWT_PRIVATE_KEY: SecretStr = SecretStr(config("JWT_PRIVATE_KEY", cast=str))  # type: ignore
    JWT_SUBJECT: str = config("JWT_SUBJECT", cast=str)  # type: ignore
    ACCESS_TOKEN_EXPIRES_IN: str = config("ACCESS_TOKEN_EXPIRES_IN", cast=str)  # type: ignore
    REFRESH_TOKEN_EXPIRES_IN: str = config("REFRESH_TOKEN_EXPIRES_IN", cast=str)  # type: ignore

    IS_ALLOWED_CREDENTIALS: bool = config("IS_ALLOWED_CREDENTIALS", cast=bool)  # type: ignore
    ALLOWED_ORIGINS: list[str] = [
        config("CLIENT_ORIGIN_LOCALHOST", cast=str),  # type: ignore
        config("CLIENT_ORIGIN_DOCKER", cast=str),  # type: ignore
    ]
    ALLOWED_METHODS: list[str] = [config("METHOD", cast=str)]  # type: ignore
    ALLOWED_HEADERS: list[str] = [config("HEADER", cast=str)]  # type: ignore

    LOGGING_LEVEL: int = logging.INFO
    LOGGERS: tuple[str, str] = ("uvicorn.asgi", "uvicorn.access")

    BCRYPT_HASHING_ALGORITHM: str = config("BCRYPT_HASHING_ALGORITHM", cast=str)  # type: ignore
    ARGON2_HASHING_ALGORITHM: str = config("ARGON2_HASHING_ALGORITHM", cast=str)  # type: ignore
    SHA256_HASHING_ALGORITHM: str = config("SHA256_HASHING_ALGORITHM", cast=str)  # type: ignore
    SHA512_HASHING_ALGORITHM: str = config("SHA512_HASHING_ALGORITHM", cast=str)  # type: ignore
    HASHING_SALT: str = config("HASHING_SALT", cast=str)  # type: ignore
    PWD_ALGORITHM_LAYER_1: str = config("PWD_ALGORITHM_LAYER_1", cast=str)  # type: ignore
    PWD_ALGORITHM_LAYER_2: str = config("PWD_ALGORITHM_LAYER_2", cast=str)  # type: ignore
    JWT_ALGORITHM: str = config("JWT_ALGORITHM", cast=str)  # type: ignore

    class Config(BaseConfig):
        case_sensitive: bool = True
        env_file: str = f"{str(Path().resolve())}/.env"
        validate_assignment: bool = True

    @property
    def set_backend_app_attributes(self) -> dict[str, str | bool | None]:
        """
        Set all `FastAPI` instance attributes with the custom values defined in `Settings`.
        """
        return {
            "title": self.TITLE,
            "version": self.VERSION,
            "debug": self.DEBUG,
            "description": self.DESCRIPTION,
            "docs_url": self.DOCS_URL,
            "openapi_url": self.OPENAPI_URL,
            "redoc_url": self.REDOC_URL,
            "openapi_prefix": self.OPENAPI_PREFIX,
            "api_prefix": self.API_PREFIX,
        }
