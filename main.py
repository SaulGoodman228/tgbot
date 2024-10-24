import telebot
import requests
from telebot.types import Message

bot = telebot.TeleBot('8069464680:AAEoiaYqjz4zFNqF5MRxB2zGbCg9jHiyxQ8')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет !')


def get_objects_from_webpage(username: str):
    url = 'http://94.228.112.181:8002//get'
    try:
        response = requests.post(url, json={"username": username})
        response.raise_for_status()
        objects = response.json()
        return objects
    except requests.exceptions.RequestException as e:
        return f"Ошибка при получении данных: {e}"

def from_dict(my_dict):
    s = my_dict['objects']
    message = ''
    for index, value in enumerate(s):
        message+=s[index]['class'] + " "
    return message

@bot.message_handler(commands=['get'])
def send_objects(message: Message):
    objects = get_objects_from_webpage(message.from_user.username)
    if isinstance(objects, str):
        bot.send_message(message.chat.id, objects)
    else:
        bot.send_message(message.chat.id, f"Объекты: {objects}")

bot.polling()