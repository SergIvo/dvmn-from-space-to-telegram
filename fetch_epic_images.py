import os
from argparse import ArgumentParser
from datetime import datetime
import requests
from dotenv import load_dotenv


def fetch_nasa_epic(images_dir, api_key):
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    params = {'api_key': api_key}
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
    api_key = os.getenv('NASA_API_KEY')
    arg_parser = ArgumentParser()
    arg_parser.add_argument('-d', dest='directory', help='Path to directory there images should be loaded')
    args = arg_parser.parse_args()

    if args.directory:
        fetch_nasa_epic(args.directory, api_key)
    else:
        fetch_nasa_epic(os.getcwd(), api_key)