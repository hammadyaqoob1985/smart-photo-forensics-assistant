import uvicorn
from fastapi import FastAPI, File, Form, UploadFile
from graph.analyze_graph import graph
import boto3
from botocore.exceptions import NoCredentialsError
import io
from config.config import Config
from langchain_core.messages import HumanMessage

app = FastAPI()

session = boto3.session.Session(
    aws_access_key_id=Config.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=Config.AWS_SECRET_ACCESS_KEY,
    region_name=Config.AWS_DEFAULT_REGION
)
s3 = session.client("s3")

@app.post("/edit-photo/")
async def upload_file(
        conversation_id: str = Form(...),
        file: UploadFile = File(...)
):
    try:
        file_content = await file.read()
        file_obj = io.BytesIO(file_content)
        s3.upload_fileobj(file_obj, Config.S3_BUCKET_NAME, file.filename, ExtraArgs={"ACL": "private"})
        image_url = f"https://{Config.S3_BUCKET_NAME}.s3.{Config.AWS_DEFAULT_REGION}.amazonaws.com/{file.filename}"
    except NoCredentialsError:
        raise RuntimeError("AWS credentials not found. Check your .env file.")

    inputs = [HumanMessage(content=f"Here is the filename: {file.filename}. Please analyze it and provide insights.")]
    config = {"recursion_limit": 25, "configurable": {"thread_id": conversation_id}}
    state = {'messages': inputs, 's3_bucket_original_url': image_url, 'filename': file.filename}
    result = graph.invoke(input=state, config=config)
    latest_message = result['messages'][-1] if result['messages'] else None
    return {"result": latest_message.content}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)