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

Run `main.py` with a `-d` flag and a directory name as an argument:
```
python main.py -d images
```
Or run `main.py` without arguments if you want application to download images first.