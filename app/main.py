from fastapi import FastAPI
from app.api.endpoints import router



app = FastAPI(title="Data Ingestion API")


app.include_router(router)
