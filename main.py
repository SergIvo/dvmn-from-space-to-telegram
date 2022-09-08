import os
from pathlib import Path
from dotenv import load_dotenv
from fetch_spacex_images import fetch_spacex_last_launch
from fetch_apod_images import fetch_nasa_apod
from fetch_epic_images import fetch_nasa_epic


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


