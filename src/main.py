from fastapi import FastAPI
from .logging import configure_logging, LogLevels
from auth.router import router as auth_router
from user.router import router as user_router


configure_logging(log_level=LogLevels.info)

app = FastAPI()

app.include_router(auth_router)
app.include_router(user_router)