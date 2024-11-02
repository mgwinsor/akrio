from fastapi import FastAPI

from .controllers.transaction_controller import router
from .database import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router, prefix="/api/v1")
