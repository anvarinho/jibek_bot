import logging
import os
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils.executor import start_webhook
from aiogram import Bot, types
from time import sleep

TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

HEROKU_APP_NAME = os.getenv('PROJECT_NAME')

# webhook settings
WEBHOOK_HOST = f'https://{HEROKU_APP_NAME}.herokuapp.com'
WEBHOOK_PATH = f'/webhook/{TOKEN}'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

# webserver settings
WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = os.getenv('PORT', default=8000)


async def on_startup(dispatcher):
    await bot.set_webhook(WEBHOOK_URL, drop_pending_updates=True)


async def on_shutdown(dispatcher):
    await bot.delete_webhook()


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    #keyboard = types.ReplyKeyboardMarkup()
    #button_1 = types.KeyboardButton(text="С пюрешкой")
    #keyboard.add(button_1)
    #button_2 = "Без пюрешки"
    #keyboard.add(button_2)
    
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    services = types.KeyboardButton(services)
    address = types.KeyboardButton(address)
    contacts = types.KeyboardButton(contacts)
    about = types.KeyboardButton(about_me)
    text = f'Привет, <b>{message.from_user.first_name}</b> ☺️\nЯ Чат-Бот Жибек 🤖!'
    keyboard.add(services, address, contacts, about)
    photo = open("kitten3.jpg", "rb")

    await message.answer(text, reply_markup=keyboard, parse_mode="html")
    sleep(0.5)
    await message.answer_photo(photo)
    sleep(0.5)
    await message.answer("Чем я могу тебе помочь?")

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        skip_updates=True,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )
