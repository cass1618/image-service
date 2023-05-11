import boto3
import base64

s3 = boto3.client("s3")


def lambda_handler(event, context):
    img = s3.get_object(
        Bucket="blackjack-images-cs-361", Key=event["imageID"]
    )["Body"].read()

    b64 = base64.b64encode(img).decode('utf-8')

    response = {
        "statusCode": 200,
        "data": b64,
    }
    return response
