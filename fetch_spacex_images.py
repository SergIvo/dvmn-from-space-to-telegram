import os
from argparse import ArgumentParser
import requests
from common import download_image


def fetch_spacex_last_launch(directory, launch_id=None):
    if launch_id:
        response = requests.get(f'https://api.spacexdata.com/v5/launches/{launch_id}')
        response.raise_for_status()
        urls_to_images = response.json()['links']['flickr']['original']
    else:
        response = requests.get('https://api.spacexdata.com/v5/launches/')
        response.raise_for_status()
        launches_with_images = [launch for launch in response.json() if launch['links']['flickr']['original']]
        urls_to_images = launches_with_images[0]['links']['flickr']['original']
    for i, image_url in enumerate(urls_to_images):
        download_image(image_url, os.path.join(directory, f'spacex_{i}.jpg'))


if __name__ == '__main__':
    arg_parser = ArgumentParser()
    arg_parser.add_argument('-i', dest='id', help='SpaceX launch ID')
    arg_parser.add_argument('-d', dest='directory', help='Path to directory there images should be loaded')
    args = arg_parser.parse_args()

    if args.directory:
        images_directory = args.directory
    else:
        images_directory = os.getcwd()
    if not args.id:
        fetch_spacex_last_launch(images_directory)
    else:
        fetch_spacex_last_launch(images_directory, launch_id=args.id)
