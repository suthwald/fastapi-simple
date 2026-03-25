from fastapi import FastAPI
from fastapi_simple.api import router

app = FastAPI(title="FastAPI Simple")

app.include_router(router)
