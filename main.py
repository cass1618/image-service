import api_requests

# uploadImage(file_path, image_id)
api_requests.uploadImage("image.png", "image1")

# getImage(imageId)
img = api_requests.getImage("image1")

# PIL methods can now be used on the object
img.show()

# view list of all image keys
img_list = api_requests.listImages()
