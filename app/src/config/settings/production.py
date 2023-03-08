from src.config.settings.environment import Environment
from src.config.settings.settings import Settings


class ProductionSettings(Settings):
    ENVIRONMENT: Environment = Environment.PRODUCTION
