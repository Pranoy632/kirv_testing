import requests


def verify_image(image_element):
    response = requests.head(image_element.get_attribute('src'))
    if response.status_code == 200:
        print(True)
    else:
        print(response.status_code)
