import os
from argparse import ArgumentParser
import requests
from downloading import download_image, get_extension
from dotenv import load_dotenv


def fetch_nasa_apod(directory, api_key):
    url = 'https://api.nasa.gov/planetary/apod'
    params = {'api_key': api_key, 'count': 30}
    response = requests.get(url, params=params)
    response.raise_for_status()
    image_urls = [apod['url'] for apod in response.json()]
    for i, image_url in enumerate(image_urls):
        if get_extension(image_url):
            filename = f'nasa_apod_{i}{get_extension(image_url)}'
            download_image(image_url, os.path.join(directory, filename))


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

    fetch_nasa_apod(args.directory, api_key)
