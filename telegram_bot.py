import os
from random import shuffle
from time import sleep
import telegram
from dotenv import load_dotenv


def send_images_to_tg(api_key, channel_id, image_directory, delay):
    bot = telegram.Bot(token=api_key)
    all_images = []
    path_to_directory = os.path.join(os.getcwd(), image_directory)
    for dir in os.walk(path_to_directory):
        paths = [os.path.join(dir[0], file) for file in dir[2]]
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

    bot = telegram.Bot(token=api_key)
    bot.send_message(chat_id=channel_id, text='Here comes picture!')

    path_to_images = os.path.join(os.getcwd(), 'images')
    if os.path.exists(path_to_images):
        images = os.listdir(path_to_images)
        with open(os.path.join(path_to_images, images[0]), 'rb') as file:
            bot.send_document(chat_id=channel_id, document=file)
    else:
        bot.send_message(chat_id=channel_id, text='No pictures :(')
