from fastapi import FastAPI # type: ignore
import motor.motor_asyncio
import beanie
from app.core.config import settings
from app.models.user_model import User
from app.api.router import router

app=FastAPI(
    title=settings.PROJECT_NAME
) 

@app.get("/")
async def hello():
    return {"message":"Hello, world"}


@app.on_event("startup")
async def app_init():
    """
        initialize MongoDB services
    """

    db_client = motor.motor_asyncio.AsyncIOMotorClient(settings.MONGO_CONNECTION_STRING)

    await beanie.init_beanie(
        database=db_client.task_db,
        document_models=[User]
    )

app.include_router(router, prefix="/api")
