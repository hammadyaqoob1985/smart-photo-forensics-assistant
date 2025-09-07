import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

class Config:
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_DEFAULT_REGION = os.getenv("AWS_DEFAULT_REGION", "us-east-1")
    S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")
    FLASK_ENV = os.getenv("FLASK_ENV", "production")

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)