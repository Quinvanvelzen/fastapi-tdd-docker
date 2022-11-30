import logging

from functools import lru_cache
from pydantic import BaseSettings

log = logging.getLogger("uvicorn")

class Settings(BaseSettings):
    environment: str = "prod"
    testing: bool = 1

@lru_cache()
def get_settings() -> BaseSettings:
    log.info("Loading config settings from environment...")
    return Settings()



