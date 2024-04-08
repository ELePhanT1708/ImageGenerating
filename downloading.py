import requests
from PIL import Image
from io import BytesIO


def download_image(url, file_path):
    # Send a GET request to the URL to fetch the image data
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Open the image data as an image object
        image = Image.open(BytesIO(response.content))

        # Save the image as a JPEG file
        image.save(file_path, 'PNG')
        print(f"Image saved as {file_path}")
    else:
        print("Failed to download image")

if __name__ == '__main__':

    # URL of the image to download
    image_url = "https://basket-02.wbbasket.ru/vol216/part21692/21692991/images/big/1.jpg"

    # File path to save the image
    file_path = "downloaded_image.jpg"

    # Download the image and save it
    download_image(image_url, file_path)
