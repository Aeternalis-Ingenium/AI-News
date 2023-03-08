from typing import AsyncGenerator

from asgi_lifespan import LifespanManager
from fastapi import FastAPI
from httpx import AsyncClient
from pytest import fixture

from src.config.settings.settings import Settings
from src.config.setup import SettingsFactory
from src.main import initialize_application


def get_test_settings() -> Settings:
    return SettingsFactory(environment="TEST")()


@fixture(name="test_app")
def test_app() -> FastAPI:
    """
    A fixture to initialize FastAPI instance as test application.
    """
    return initialize_application()


@fixture(name="initialize_test_application")
async def initialize_test_application(test_app: FastAPI) -> AsyncGenerator[FastAPI, None]:
    async with LifespanManager(test_app):
        yield test_app


@fixture(name="async_client")
async def async_client(initialize_test_application: FastAPI) -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(
        app=initialize_test_application,
        base_url="http://testserver",
        headers={"Content-Type": "application/json"},
    ) as client:
        yield client
