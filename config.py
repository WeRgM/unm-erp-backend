import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DB_USERNAME = os.getenv('DB_USERNAME')
    DB_PASSWORD = os.getenv('DB_USERNAME')
    DB_SERVER = os.getenv('DB_USERNAME')
    DB_NAME = os.getenv('DB_USERNAME')
    DB_DRIVER= os.getenv('DB_DRIVER')

    SQLALCHEMY_DATABASE_URI = f'mssql+pyodbc://{DB_USERNAME}:{DB_PASSWORD}@{DB_SERVER}/{DB_NAME}?driver={DB_DRIVER}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
