from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.upload_service import process_upload_file

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Welcome to Data Ingestion API"}

@router.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    try:
        message = process_upload_file(file)
        return {"message": message}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
