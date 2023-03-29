# project/app/api/ping.py

from fastapi import APIRouter, Depends

from app.config import Settings, get_settings

router = APIRouter()


@router.get("/ping")
async def pong(settings: Settings = Depends(get_settings)):
    return {
        "ping": "pong!",
        "environment": settings.environment,
        "testing": settings.testing,
    }


@router.get("/quinten_addition")
async def root(message: str):
    return {
        message: message + " <- this message will make the world a better place",
        "hey Quinten, how are you?": "Hey user, thank you for asking, I am good!",
    }
