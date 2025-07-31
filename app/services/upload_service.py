import pandas as pd
from app.db.session import engine
from app.utils.file_utils import save_temp_file, cleanup_file

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    # Example minimal transform (customize as needed)
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    # Here you can add validation, type casting, filling missing values, etc.
    return df

def process_upload_file(upload_file) -> str:
    temp_path = save_temp_file(upload_file)
    try:
        # Extract
        if upload_file.filename.endswith(".csv"):
            df = pd.read_csv(temp_path)
        elif upload_file.filename.endswith((".xls", ".xlsx")):
            df = pd.read_excel(temp_path)
        else:
            raise ValueError("Unsupported file format. Only CSV and Excel allowed.")

        if df.empty:
            raise ValueError("Uploaded file is empty.")

        # Transform
        df = transform_data(df)

        # Load
        df.to_sql("courier_data", con=engine, if_exists="replace", index=False)
        return "File processed and data uploaded to PostgreSQL successfully."
    finally:
        cleanup_file(temp_path)
