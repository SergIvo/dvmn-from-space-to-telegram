# Space Pictures To Telegram

## About

The application works as a bot what sends images from provided directory to certain Telegram channel. Application runs from command line accepting name of directory with images as argument. If no directory is provided, application creates one and populates it with images fetched from SpaceX and NASA open APIs.

This application created for educational purposes as part of an online course for web developers at [dvmn.org](https://dvmn.org/)

## Running the application

1. Download application files from GitHub using `git clone` command:
```
git clone https://github.com/SergIvo/dvmn-from-space-to-telegram
```
2. Create virtual environment with python [venv](https://docs.python.org/3/library/venv.html) library to avoid conflicts with other versions of the same packages:
```
python -m venv venv
```
Then install dependencies from "requirements.txt" in created virtual environment using `pip` package manager:
```
pip install -r requirements.txt
```
To run application, you should also first set a few environment variables:
```
export NASA_API_KEY="your NASA API key"
export TG_API_KEY="your Telegram API key"
export CHANNEL_ID="id of a Telegram channel"
export DELAY="posting time interval"
```
Having NASA API key set is not necessary if you specify directory with images when run application. Otherwise application will require this API key to get images from NASA open API.

`DELAY` is the time in seconds what bot waits before post next image. If not provided, this time is set to 4 hours.

To make environment variable management easier, you can create [.env](https://pypi.org/project/python-dotenv/#getting-started) file and store all variables in it. 

To make application constantly post images from certain directory to Telegram channel, run `main.py` with a `-d` flag and a directory name as an argument:
```
python main.py -d images
```
Or run `main.py` without arguments if you want application to download images first.

To post one specified image, run `telegram_bot.py` with `-i` flag and path to image as argument:
```
python telegram_bot.py -i images/nasa_apod_6.jpg
```
To download photos of SpaceX launch to specified directory, run `fetch_spacex_images.py` with flag `-d` and directory name as argument. To download photos of specified launch, add flag `-i` and launch ID as argument. If no launch ID provided, photos from last launch with photographs will be downloaded. If directory is not specified, images will be saved in current directory.
```
python fetch_spacex_images.py -d images -i 5eb87ce4ffd86e000604b337
```
To download NASA APOD images to specified directory, run `fetch_apod_images.py` with flag `-d` and directory name as argument.
```
python fetch_apod_images.py -d images
```
To download NASA EPIC images to specified directory, run `fetch_epic_images.py` with flag `-d` and directory name as argument.
```
python fetch_epic_images.py -d images
```