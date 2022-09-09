import os
from random import shuffle, choice
from time import sleep
from argparse import ArgumentParser
import telegram
from dotenv import load_dotenv


def send_images_to_tg(api_key, channel_id, image_directory, delay):
    bot = telegram.Bot(token=api_key)
    all_images = []
    path_to_directory = os.path.join(os.getcwd(), image_directory)
    for subdirectory in os.walk(path_to_directory):
        base_path, __, files = subdirectory
        paths = [os.path.join(base_path, file) for file in files]
        all_images.extend(paths)
    counter = 0
    while True:
        if counter == len(all_images):
            shuffle(all_images)
            counter = 0
        image = all_images[counter]
        if os.stat(image).st_size < 20971520 and os.stat(image).st_size != 0:
            with open(image, 'rb') as file:
                bot.send_document(chat_id=channel_id, document=file)
        counter += 1
        sleep(delay)


if __name__ == '__main__':
    load_dotenv()
    api_key = os.getenv('TG_API_KEY')
    channel_id = os.getenv('CHANNEL_ID')
    arg_parser = ArgumentParser()
    arg_parser.add_argument('-i', dest='image', help='Image to load')
    args = arg_parser.parse_args()

    bot = telegram.Bot(token=api_key)
    path_to_images = os.path.join(os.getcwd(), 'images')
    if args.image:
        with open(os.path.join(os.getcwd(), args.image), 'rb') as file:
            bot.send_document(chat_id=channel_id, document=file)
    elif os.path.exists(path_to_images):
        images = os.listdir(path_to_images)
        with open(os.path.join(path_to_images, choice(images)), 'rb') as file:
            bot.send_document(chat_id=channel_id, document=file)
    else:
        bot.send_message(chat_id=channel_id, text='No pictures :(')
