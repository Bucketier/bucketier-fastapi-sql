from fastapi import FastAPI
from src.database import Base, engine
from src.logging import configure_logging, LogLevels
from src.auth.router import router as auth_router
from src.user.router import router as user_router


configure_logging(log_level=LogLevels.info)

app = FastAPI()

app.include_router(auth_router)
app.include_router(user_router)


Base.metadata.create_all(bind=engine)