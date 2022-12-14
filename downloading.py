import os
from urllib.parse import urlsplit, unquote
import requests


def download_image(url, path, params=None):
    response = requests.get(url, params=params)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)


def get_extension(url):
    splitted = urlsplit(url)
    path = unquote(splitted.path)
    return os.path.splitext(path)[1]
