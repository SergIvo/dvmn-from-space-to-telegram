import os
from argparse import ArgumentParser
from datetime import datetime
import requests
from dotenv import load_dotenv
from downloading import download_image


def fetch_nasa_epic(images_dir, api_key):
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    params = {'api_key': api_key}
    response = requests.get(url, params=params)
    response.raise_for_status()
    recent_images = response.json()
    for image in recent_images:
        filename = f"{image['image']}.png"
        image_datetime = datetime.fromisoformat(image['date'])
        image_date = image_datetime.strftime('%Y/%m/%d')
        image_url = f'https://api.nasa.gov/EPIC/archive/natural/{image_date}/png/{filename}'
        image_path = os.path.join(images_dir, filename)
        download_image(image_url, image_path, params=params)


if __name__ == '__main__':
    load_dotenv()
    api_key = os.getenv('NASA_API_KEY')
    arg_parser = ArgumentParser()
    arg_parser.add_argument(
        '-d',
        dest='directory',
        default=os.getcwd(),
        help='Path to directory there images should be loaded'
    )
    args = arg_parser.parse_args()

    fetch_nasa_epic(args.directory, api_key)
