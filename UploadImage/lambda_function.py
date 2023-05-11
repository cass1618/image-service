import json
import boto3
import base64

s3 = boto3.client("s3")


def lambda_handler(event, context):
    b64img = event["base64Image"]
    img = base64.b64decode(b64img)

    s3.put_object(Body=img, Bucket="blackjack-images-cs-361", Key=event["imageId"])

    response = {
        "statusCode": 200,
        "message": "successfully uploaded file"
    }

    return response
