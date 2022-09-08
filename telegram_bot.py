import os
import telegram
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv('TG_API_KEY')
channel_id = os.getenv('CHANNEL_ID')
bot = telegram.Bot(token=api_key)
bot.send_message(chat_id=channel_id, text='Nevermind.')