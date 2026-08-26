from fastapi import FastAPI
from .logging import configure_logging, LogLevels

configure_logging(log_level=LogLevels.info)

app = FastAPI()