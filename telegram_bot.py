import os
from random import choice
import telegram
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv('TG_API_KEY')
channel_id = os.getenv('CHANNEL_ID')

bot = telegram.Bot(token=api_key)
bot.send_message(chat_id=channel_id, text='Here comes picture!')

path_to_images = os.path.join(os.getcwd(), 'images')
random_image = choice(os.listdir(path_to_images))
with open(os.path.join(path_to_images, random_image), 'rb') as file:
    bot.send_document(chat_id=channel_id, document=file)
