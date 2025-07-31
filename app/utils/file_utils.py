import shutil
import os

def save_temp_file(upload_file) -> str:
    temp_path = f"temp_{upload_file.filename}"
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(upload_file.file, buffer)
    return temp_path

def cleanup_file(path: str):
    if os.path.exists(path):
        os.remove(path)
