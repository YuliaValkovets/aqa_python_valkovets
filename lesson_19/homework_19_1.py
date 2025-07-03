import requests

url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}

response = requests.get(url, params=params)
if response.status_code == 200:
    data = response.json()
    photos = data.get('photos')

    for k, photo in enumerate(photos):
        url_photo = photo['img_src']
        image = requests.get(url_photo)
        filename = f"mars_photo{k + 1}.jpg"

        with open(filename, 'wb') as img:
            img.write(image.content)
            print(f"The image was downloaded successfully: {filename}")
else:
    print("Request error: ", response.status_code)