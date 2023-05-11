import boto3
import json

s3 = boto3.resource("s3")
bucket = s3.Bucket("blackjack-images-cs-361")


def lambda_handler(event, context):
    img_list = []
    for item in bucket.objects.all():
        img_list.append(item.key)

    return {
        'statusCode': 200,
        'data': json.dumps(img_list)
    }
