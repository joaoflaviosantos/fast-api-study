'''Instancing the FastAPI class and include routes from APIRouter instances'''
from fastapi import FastAPI

# pylint: disable=pointless-string-statement
# pylint: disable=invalid-name
# pylint: disable=import-error

from routes.first_steps import router as first_steps

app = FastAPI(title="FastAPI, PostgreSQL, SQLAlchemy, AIOHTTP")

app.include_router(router=first_steps, prefix="", tags=["first-steps"])
    