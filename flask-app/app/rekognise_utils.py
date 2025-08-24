import boto3
from .config import Config

rekognition_client = boto3.client("rekognition", region_name=Config.AWS_DEFAULT_REGION)

def analyze_image(image_key):
    """
    Uses AWS Rekognition to detect labels/objects in an image.
    """
    response = rekognition_client.detect_labels(
        Image={"S3Object": {"Bucket": Config.S3_BUCKET_NAME, "Name": image_key}},
        MaxLabels=10,
        MinConfidence=75
    )

    return [
        {"name": label["Name"], "confidence": round(label["Confidence"], 2)}
        for label in response["Labels"]
    ]