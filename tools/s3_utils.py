import boto3
from botocore.exceptions import NoCredentialsError
from langchain.agents import tool
from config.config import Config

session = boto3.session.Session(
    aws_access_key_id=Config.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=Config.AWS_SECRET_ACCESS_KEY,
    region_name=Config.AWS_DEFAULT_REGION
)
s3 = session.client("s3")

@tool
def upload_file_to_s3(file_obj, filename):
    """Uploads a file object to S3 and returns its URL."""
    try:
        s3.upload_fileobj(file_obj, Config.S3_BUCKET_NAME, filename, ExtraArgs={"ACL": "private"})
        return f"https://{Config.S3_BUCKET_NAME}.s3.{Config.AWS_DEFAULT_REGION}.amazonaws.com/{filename}"
    except NoCredentialsError:
        raise RuntimeError("AWS credentials not found. Check your .env file.")

def list_files_in_s3():
    response = s3.list_objects_v2(Bucket=Config.S3_BUCKET_NAME)
    return [obj["Key"] for obj in response.get("Contents", [])] if "Contents" in response else []

def download_file_from_s3(filename):
    try:
        file_obj = s3.get_object(Bucket=Config.S3_BUCKET_NAME, Key=filename)
        return file_obj["Body"].read()
    except s3.exceptions.NoSuchKey:
        return None
