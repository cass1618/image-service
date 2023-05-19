import requests
from PIL import Image
from io import BytesIO
import base64
import json


def getImage(image_id):
    # api GET endpoint with imageID query parameter
    url = f"https://5p53jt8p6e.execute-api.us-west-2.amazonaws.com/images/?imageID={image_id}"

    # send get request
    response = requests.get(url)

    if response.json()['statusCode'] == 200:
        # response returns a base64 encoded string
        base64_string = response.json()['data']

        # convert string to a BytesIO object for use with PIL
        image_file = BytesIO(base64.b64decode(base64_string))

        # convert BytesIO object to Image object
        image = Image.open(image_file)
        return image

    elif response.json()['statusCode'] == 413:
        print("image not found")

    else:
        print("unknown error")


def uploadImage(file_path, image_id):
    # api POST endpoint
    url = "https://5p53jt8p6e.execute-api.us-west-2.amazonaws.com/images/"

    # open image file and decode to base64
    with open(file_path, "rb") as image:
        b64_string = base64.b64encode(image.read()).decode("utf-8")

    # body of post request must contain base64 encoded image and desired imageID
    body = {
        "imageId": image_id,
        "base64Image": b64_string
    }

    # send post request
    try:
        response = requests.post(url, json=body)
        response.raise_for_status()
        print("successfully uploaded image")
    except requests.exceptions.HTTPError as error:
        print("file too large - max size 4MB") \
            if response.status_code == 413 \
            else print("unspecified error: ", error)


def listImages():
    # api GET endpoint
    url = "https://5p53jt8p6e.execute-api.us-west-2.amazonaws.com/images/list"

    # extracts list of image keys from response
    image_list = json.loads(requests.get(url).json()['data'])

    # print each image key
    for image in image_list:
        print(image)

    # return the list
    return image_list
