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



start = "/start"

back = "Назад ↩️"

brows = "Брови 😌"

lashes = "Ресницы 👁"

services = "Виды Услуг 📜"

address = "Адрес 🏛"

ADDRESS = f"Москва, метро и МЦК Дубровка, \nул. Шарикоподшипниковская, 2️⃣2️⃣,\nподъезд 5️⃣,\nкод подъезда(5️⃣🔑1️⃣9️⃣4️⃣5️⃣),\n4️⃣ этаж,\nдверь 🚪5️⃣4️⃣2️⃣"

contacts = "Контакты 📱"

CONTACTS = "Мой номер телефона +79999788423 (по этому номеру доступен WhatsApp и Telegram). Большинство моих работ на странице Инстаграм (который доступен через VPN 😁)"

about_me = "Обо мне 📠"

ABOUT_ME = "Привет✌️, я Жибек (можно Женя если сложно😂) твой мастер по бровям и ресничкам. Сделаю ваш взгляд эффектнее и привлекательнее😌. А бровки как с обложки глянцевого журнала😎."

pm_main = "Основная процедура"

PM_MAIN = "Основная процедура ПМ бровей - мастер  рассказывает вам про противопоказания, подбирает и рисует эскиз ваших будущих бровей, исходя из природных данных и пожеланий модели. Есть возможность выбрать оттенок пигмента с которым будет проходить процедура напыления⚡️ ...."

pm_corr = "Коррекция"

PM_CORR = "Коррекция - процедура выполняется через 28 дней после основной процедуры, так как за этот период происходит полная регенерация кожи. Она проходит точно также как и основная процедура, для закрепления пигмента на более длительный срок💥."

remove_pm = "Перекрытие"

REMOVE_PM = "Удаление старого татуажа."

notice = "Примечание"

NOTICE = "Процедура напыления бровей происходит путём введения пигмента в верхний слой кожи тонкими одноразовыми картриджами (иглами). Поэтому есть противопоказания для тех, у кого есть заболевания связанные с кожным покровом (все виды аллергии),🛑 свёртываемостью крови (ВИЧ, СПИД, сахарный диабет),⛔️ поздние месяцы беременности.⛔️ Процедура проходит в два этапа, для того, чтобы закрепить результат на максимальный срок.🌞"

lashes_procedure = ""

classic = "Классическое 🖤"

CLASSIC = "Классическое наращивание 🌸 - к каждой родной ресничке мы прикрепляем одну искусственную ресничку 😊, тем самым просто слегка подчеркиваем ваши натуральные ресницы....."

one_five = "1️⃣.5️⃣D 💄"

ONE_FIVE = "Объём 1️⃣.5️⃣D 😇 - это способ наращивания ресниц, где мы чередуем пучок из двух ресниц и одну искусственную, также по вашему желанию можем сделать акцент на внешний угол глаз и ставить пучки только там 🥰....."

two = "2️⃣D 💋"

TWO = "Объём 2️⃣D 🔥 (самое популярное) -  к каждой родной ресничке мы клеим две искусственные реснички, создавая из них пучок (вручную) тем самым увеличиваем количество ваших родных ресниц в два раза🥰......."

two_five = "2️⃣.5️⃣D ❤️‍🔥"

TWO_FIVE = "Объём 2️⃣.5️⃣D 🏵 - в этом виде наращивания мы чередуем пучки из двух и трёх искусственных ресниц, также по вашему желанию можно сделать акцент на внешний угол глаз и клеить тройные пучки только там🧚🏽‍♀️ ...."

three = "3️⃣D 🍉"

THREE = "Объём 3️⃣D ❤️ - в этом виде наращивания мы приклеиваем пучок из трёх искусственных ресниц к каждой родной реснице, в итоге получаем пушистые объёмные ресницы 🥳 ......"

hollywood = "Hollywood ✨"

HOLLYWOOD = "Hollywood ❤️ - самый объёмный вид наращивания пучками 4️⃣D-5️⃣D 😍......"

extra = "Дополнительно 📜"

curve_l = "Изгиб L"

CURVE_L = "Изгиб L - один из самых популярных изгибов который подходит абсолютно всем, особенно для любителей подводок и стрелок. Также его полюбят те кто носит очки😍."

curve_m = "Изгиб M"

CURVE_M = "Изгиб M - подойдёт для тех у кого нависшее веко или глубоко посаженные глаза....."

spec_wide = "Толщина 0.07"

SPEC_WIDE = "Толщина 0.07 - тоненькие, невесомые легкие ресницы очень удобны для объемного наращивания также им можно добиться нереально красивого натурального эффекта"

fixer = "Закрепитель"

FIXER = "Закрепитель наносится для того, чтобы увеличить срок носки наращенных ресниц. Он усиливает эффект сцепки родной и искусственной реснички 🌞...."

kylie_effect = "Эффект Kylie"

KYLIE_EFFECT = "Эффект Kylie (лучики) 🌅 - в стиле известной модели Кайли Дженнер. В таком эффекте используют разреженное наращивание. Сначала производится обычное наращивание, а затем вставляем лучики длиннее основного наращивания ⚡️....."

remove_lashes = "Снятие ресниц"

REMOVE_LASHES = "Процесс снятия производится кремовым ремувером (самый щадящий ремувер) без жжения и дискомфорта."
