import os
from pathlib import Path
from argparse import ArgumentParser
from dotenv import load_dotenv
from fetch_spacex_images import fetch_spacex_last_launch
from fetch_apod_images import fetch_nasa_apod
from fetch_epic_images import fetch_nasa_epic
from telegram_bot import send_images_to_tg


if __name__ == '__main__':
    load_dotenv()
    nasa_api_key = os.getenv('NASA_API_KEY')
    tg_api_key = os.getenv('TG_API_KEY')
    channel_id = os.getenv('CHANNEL_ID')
    if os.getenv('DELAY'):
        delay = int(os.getenv('DELAY'))
    else:
        delay = 14400

    arg_parser = ArgumentParser()
    arg_parser.add_argument('-d', dest='directory', help='Directory with images that should be posted')
    args = arg_parser.parse_args()

    if args.directory:
        send_images_to_tg(tg_api_key, channel_id, args.directory, delay)
    else:
        images_directory = Path('images')
        images_directory.mkdir(parents=True, exist_ok=True)

        fetch_spacex_last_launch(images_directory)
        fetch_nasa_apod(images_directory, nasa_api_key)
        fetch_nasa_epic(images_directory, nasa_api_key)
        send_images_to_tg(tg_api_key, channel_id, images_directory, delay)
