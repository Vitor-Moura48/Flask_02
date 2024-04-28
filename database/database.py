from peewee import PostgresqlDatabase
from dotenv import load_dotenv
import os

load_dotenv()
db = PostgresqlDatabase(os.getenv('DATABASE_URI', ''))