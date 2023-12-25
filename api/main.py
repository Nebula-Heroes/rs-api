
import os
from fastapi import FastAPI
from sqlalchemy.orm import sessionmaker
import sqlalchemy

POSTGRES_CONNECTION_STRING = os.getenv('POSTGRES_CONNECTION_STRING')
engine = sqlalchemy.create_engine(POSTGRES_CONNECTION_STRING)

from .routers import router as machine_router

app = FastAPI()
app.include_router(machine_router)

@app.get("/")
def root():
    """
    Returns a greeting message indicating that the RS API is up and running.

    Returns:
        dict: A dictionary containing a greeting message.
    """
    return {
        "message": "Welcome to the RS API. It is currently running and ready to serve requests.",
        "version": "1.0.0"  
    }