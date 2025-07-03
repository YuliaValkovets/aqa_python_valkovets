import requests

url = 'http://127.0.0.1:8080'

def upload_image(filename):
    with open(filename, 'rb') as image:
        files = {'image': image}
        response = requests.post(f'{url}/upload', files=files)
        if response.status_code == 201:
            print(f'The image was uploaded: {response.json()}')
        else:
            print(f"Request error: {response.status_code}")


def get_url_image(filename):
    headers = {'Content-Type': 'text'}
    response = requests.get(f'{url}/image/{filename}', headers=headers)
    if response.status_code == 200:
        data = response.json()
        url_image = data.get('image_url')
        print("Url image:", url_image)
    else:
        print(f"Request error: {response.status_code}")


def delete_image(filename):
    response = requests.delete(f'{url}/delete/{filename}')
    if response.status_code == 200:
        print("The image was deleted successfully")
    else:
        print(f"Request error: {response.status_code}")



filename = 'isewtweetbg.jpg'

upload_image(filename)
get_url_image(filename)
delete_image(filename)