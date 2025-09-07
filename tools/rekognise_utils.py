import boto3
from config.config import Config
from langchain.agents import tool
rekognition_client = boto3.client("rekognition", region_name=Config.AWS_DEFAULT_REGION)

@tool
def analyze_image(filename: str):
    """
    Uses AWS Rekognition to detect labels/objects in an image.
    """
    response = rekognition_client.detect_labels(
        Image={"S3Object": {"Bucket": Config.S3_BUCKET_NAME, "Name": filename}},
        MaxLabels=50,
        MinConfidence=50
    )

    return [
        {"name": label["Name"], "confidence": round(label["Confidence"], 2)}
        for label in response["Labels"]
    ]