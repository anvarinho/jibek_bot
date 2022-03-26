import logging
from aiogram import Bot
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
import os

TOKEN = os.environ["TOKEN"]

logging.basicConfig(level=logging.INFO)

#PORT = int(os.environ.get("PORT", 5000))
#TOKEN = os.environ("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup()
    button_1 = types.KeyboardButton(text="С пюрешкой")
    keyboard.add(button_1)
    button_2 = "Без пюрешки"
    keyboard.add(button_2)
    await bot.send_message(message.chat.id, "Hello", reply_markup=keyboard)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
