Data Ingestion API
A FastAPI-based backend application to upload CSV or Excel files, parse their contents, and store the data into a PostgreSQL database. This project demonstrates a clean, modular structure suitable for production and scalability.

Features
Upload CSV or Excel files via Swagger UI (interactive API docs)

Extract data using pandas

Basic transformation of data (column name cleaning)

Load data into PostgreSQL database using SQLAlchemy

Clear project structure adhering to Python best practices

Configurable database settings using environment variables (.env file)

Easily extendable for complex ETL pipelines

Prerequisites
Python 3.9 or higher

PostgreSQL installed and running

Basic knowledge of FastAPI and SQL databases