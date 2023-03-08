from enum import Enum


class Environment(str, Enum):
    PRODUCTION = "PROD"
    DEVELOPMENT = "DEV"
    TEST = "TEST"
