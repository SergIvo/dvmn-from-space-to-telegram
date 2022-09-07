import os
from pathlib import Path
from urllib.parse import urlsplit, unquote
from datetime import datetime
import requests
from dotenv import load_dotenv


def download_image(url, path):
    response = requests.get(url)
    response.raise_for_status()
    with open (path, 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch(images_dir):
    response = requests.get('https://api.spacexdata.com/v5/launches/')
    response.raise_for_status()
    reports_with_images = [launch for launch in response.json() if launch['links']['flickr']['original']]
    latest_images = reports_with_images[0]['links']['flickr']['original']
    for i, image_url in enumerate(latest_images):
        download_image(image_url, os.path.join(images_dir, f'spacex_{i}.jpg'))


def get_extension(url):
    splitted = urlsplit(url)
    path = unquote(splitted.path)
    return os.path.splitext(path)[1]


def fetch_nasa_apod(images_dir):
    url = 'https://api.nasa.gov/planetary/apod'
    params = {'api_key': os.getenv('NASA_API_KEY'), 'count': 30}
    response = requests.get(url, params=params)
    response.raise_for_status()
    image_urls = [apod['url'] for apod in response.json()]
    for i, image_url in enumerate(image_urls):
        filename = f'nasa_apod_{i}{get_extension(image_url)}'
        download_image(image_url, os.path.join(images_dir, filename))


def fetch_nasa_epic(images_dir):
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    params = {'api_key': os.getenv('NASA_API_KEY')}
    response = requests.get(url, params=params)
    response.raise_for_status()
    recent_images = response.json()
    for i, image in enumerate(recent_images):
        filename = f"{image['image']}.png"
        image_datetime = datetime.fromisoformat(image['date'])
        image_date = image_datetime.strftime('%Y/%m/%d')
        image_url = f'https://api.nasa.gov/EPIC/archive/natural/{image_date}/png/{filename}'
        response = requests.get(image_url, params=params)
        response.raise_for_status()
        with open(os.path.join(images_dir, filename), 'wb') as file:
            file.write(response.content)


if __name__ == '__main__':
    load_dotenv()
    images_dir = Path('images')
    images_dir.mkdir(parents=True, exist_ok=True)
    filename = 'hubble.jpg'
    url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
    download_image(url, os.path.join(images_dir, filename))
    fetch_spacex_last_launch(images_dir)
    fetch_nasa_apod(images_dir)
    fetch_nasa_epic(images_dir)


