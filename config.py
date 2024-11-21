import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    
    MYSQL_USERNAME = os.environ.get('MYSQL_USERNAME')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD')
    MYSQL_ENDPOINT = os.environ.get('MYSQL_ENDPOINT')
    MYSQL_PORT = os.environ.get('MYSQL_PORT')
    MYSQL_DB_NAME = os.environ.get('MYSQL_DB_NAME')
    
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@{MYSQL_ENDPOINT}:{MYSQL_PORT}/{MYSQL_DB_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False