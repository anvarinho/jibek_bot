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
    if message.text == back:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        services = types.KeyboardButton(services)
        address = types.KeyboardButton(address)
        contacts = types.KeyboardButton(contacts)
        about = types.KeyboardButton(about_me)
        markup.add(services, address, contacts, about)
        photo = open("kitten3.jpg", "rb")
        await message.answer_photo(photo)
        sleep(0.5)
        await message.answer("Чем я могу тебе помочь?", reply_markup=markup)

    elif message.text == services:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        lashes = types.KeyboardButton(lashes)
        brows = types.KeyboardButton(brows)
        markup.add(lashes, brows)
        await message.answer("Выберите вид услуг:", reply_markup=markup)

    elif message.text == brows:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        main = types.KeyboardButton(pm_main)
        corr = types.KeyboardButton(pm_corr)
        rem = types.KeyboardButton(remove_pm)
        notice = types.KeyboardButton(notice)
        markup.add(main, corr, rem, notice)
        await message.answer("Перманентный макияж бровей.\nВиды услуг:", reply_markup=markup)

    elif message.text == lashes:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        classic = types.KeyboardButton(classic)
        one_five = types.KeyboardButton(one_five)
        two = types.KeyboardButton(two)
        two_five = types.KeyboardButton(two_five)
        three = types.KeyboardButton(three)
        hollywood = types.KeyboardButton(hollywood)
        extra = types.KeyboardButton(extra)
        markup.add(classic, one_five, two, two_five, three, hollywood, extra)
        await message.answer("Наращивание ресниц.\nВиды услуг:", reply_markup=markup)

    elif message.text == contacts:
        markup = types.InlineKeyboardMarkup(row_width=1)
        instagram = types.InlineKeyboardButton("Мой Instagram 📸", url="https://instagram.com/browbarmsk")
        whatsapp = types.InlineKeyboardButton("Мой WhatsApp 📱", url="https://wa.me/79999788423")
        telegram = types.InlineKeyboardButton("Мой Telegram 📲", url="https://t.me/dokbaeva")
        markup.add(instagram, whatsapp, telegram)
        await message.answer(CONTACTS, reply_markup=markup)

    elif message.text == address:
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Маршрут 🗺", "https://go.2gis.com/08fgl"))
        await message.answer(ADDRESS, reply_markup=markup)

    elif message.text == about_me:
        await message.answer(ABOUT_ME)

    elif message.text == extra:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        curve_l = types.KeyboardButton(curve_l)
        curve_m = types.KeyboardButton(curve_m)
        spec_wide = types.KeyboardButton(spec_wide)
        fixer = types.KeyboardButton(fixer)
        effect = types.KeyboardButton(kylie_effect)
        remove = types.KeyboardButton(remove_lashes)
        markup.add(curve_l, curve_m, spec_wide, fixer, effect, remove)
        await message.answer("Дополнительные услуги:", reply_markup=markup)

    elif message.text == pm_main:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        main = types.KeyboardButton(services)
        corr = types.KeyboardButton(pm_corr)
        rem = types.KeyboardButton(remove_pm)
        notice = types.KeyboardButton(notice)
        markup.add(main, corr, rem, notice)
        await message.answer(PM_MAIN, reply_markup=markup)

    elif message.text == pm_corr:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        main = types.KeyboardButton(pm_main)
        corr = types.KeyboardButton(services)
        rem = types.KeyboardButton(remove_pm)
        notice = types.KeyboardButton(notice)
        markup.add(main, corr, rem, notice)
        await message.answer(PM_CORR, reply_markup=markup)

    elif message.text == remove_pm:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        main = types.KeyboardButton(pm_main)
        corr = types.KeyboardButton(pm_corr)
        rem = types.KeyboardButton(services)
        notice = types.KeyboardButton(notice)
        markup.add(main, corr, rem, notice)
        await message.answer(REMOVE_PM, reply_markup=markup)

    elif message.text == notice:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        main = types.KeyboardButton(pm_main)
        corr = types.KeyboardButton(pm_corr)
        rem = types.KeyboardButton(remove_pm)
        notice = types.KeyboardButton(services)
        markup.add(main, corr, rem, notice)
        await message.answer(NOTICE,reply_markup=markup)
    
    elif message.text == classic:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        classic = types.KeyboardButton(services)
        one_five = types.KeyboardButton(one_five)
        two = types.KeyboardButton(two)
        two_five = types.KeyboardButton(two_five)
        three = types.KeyboardButton(three)
        hollywood = types.KeyboardButton(hollywood)
        extra = types.KeyboardButton(extra)
        markup.add(classic, one_five, two, two_five, three, hollywood, extra)
        await message.answer(CLASSIC, reply_markup=markup)

    elif message.text == one_five:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        classic = types.KeyboardButton(classic)
        one_five = types.KeyboardButton(services)
        two = types.KeyboardButton(two)
        two_five = types.KeyboardButton(two_five)
        three = types.KeyboardButton(three)
        hollywood = types.KeyboardButton(hollywood)
        extra = types.KeyboardButton(extra)
        markup.add(classic, one_five, two, two_five, three, hollywood, extra)
        await message.answer(ONE_FIVE, reply_markup=markup)

    elif message.text == two:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        classic = types.KeyboardButton(classic)
        one_five = types.KeyboardButton(one_five)
        two = types.KeyboardButton(services)
        two_five = types.KeyboardButton(two_five)
        three = types.KeyboardButton(three)
        hollywood = types.KeyboardButton(hollywood)
        extra = types.KeyboardButton(extra)
        markup.add(classic, one_five, two, two_five, three, hollywood, extra)
        await message.answer(TWO, reply_markup=markup)

    elif message.text == two_five:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        classic = types.KeyboardButton(classic)
        one_five = types.KeyboardButton(one_five)
        two = types.KeyboardButton(two)
        two_five = types.KeyboardButton(services)
        three = types.KeyboardButton(three)
        hollywood = types.KeyboardButton(hollywood)
        extra = types.KeyboardButton(extra)
        markup.add(classic, one_five, two, two_five, three, hollywood, extra)
        await message.answer(TWO_FIVE, reply_markup=markup)

    elif message.text == three:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        classic = types.KeyboardButton(classic)
        one_five = types.KeyboardButton(one_five)
        two = types.KeyboardButton(two)
        two_five = types.KeyboardButton(two_five)
        three = types.KeyboardButton(services)
        hollywood = types.KeyboardButton(hollywood)
        extra = types.KeyboardButton(extra)
        markup.add(classic, one_five, two, two_five, three, hollywood, extra)
        await message.answer(THREE, reply_markup=markup)

    elif message.text == hollywood:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        classic = types.KeyboardButton(classic)
        one_five = types.KeyboardButton(one_five)
        two = types.KeyboardButton(two)
        two_five = types.KeyboardButton(two_five)
        three = types.KeyboardButton(three)
        hollywood = types.KeyboardButton(services)
        extra = types.KeyboardButton(extra)
        markup.add(classic, one_five, two, two_five, three, hollywood, extra)
        await message.answer(HOLLYWOOD, reply_markup=markup)

    elif message.text == curve_l:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        curve_l = types.KeyboardButton(back)
        curve_m = types.KeyboardButton(curve_m)
        spec_wide = types.KeyboardButton(spec_wide)
        fixer = types.KeyboardButton(fixer)
        effect = types.KeyboardButton(kylie_effect)
        remove = types.KeyboardButton(remove_lashes)
        markup.add(curve_l, curve_m, spec_wide, fixer, effect, remove)
        await message.answer(CURVE_L, reply_markup=markup)

    elif message.text == curve_m:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        curve_l = types.KeyboardButton(curve_l)
        curve_m = types.KeyboardButton(back)
        spec_wide = types.KeyboardButton(spec_wide)
        fixer = types.KeyboardButton(fixer)
        effect = types.KeyboardButton(kylie_effect)
        remove = types.KeyboardButton(remove_lashes)
        markup.add(curve_l, curve_m, spec_wide, fixer, effect, remove)
        await message.answer(CURVE_M, reply_markup=markup)

    elif message.text == spec_wide:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        curve_l = types.KeyboardButton(curve_l)
        curve_m = types.KeyboardButton(curve_m)
        spec_wide = types.KeyboardButton(back)
        fixer = types.KeyboardButton(fixer)
        effect = types.KeyboardButton(kylie_effect)
        remove = types.KeyboardButton(remove_lashes)
        markup.add(curve_l, curve_m, spec_wide, fixer, effect, remove)
        await message.answer(SPEC_WIDE, reply_markup=markup)

    elif message.text == fixer:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        curve_l = types.KeyboardButton(curve_l)
        curve_m = types.KeyboardButton(curve_m)
        spec_wide = types.KeyboardButton(spec_wide)
        fixer = types.KeyboardButton(back)
        effect = types.KeyboardButton(kylie_effect)
        remove = types.KeyboardButton(remove_lashes)
        markup.add(curve_l, curve_m, spec_wide, fixer, effect, remove)
        await message.answer(FIXER, reply_markup=markup)

    elif message.text == kylie_effect:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        curve_l = types.KeyboardButton(curve_l)
        curve_m = types.KeyboardButton(curve_m)
        spec_wide = types.KeyboardButton(spec_wide)
        fixer = types.KeyboardButton(fixer)
        effect = types.KeyboardButton(back)
        remove = types.KeyboardButton(remove_lashes)
        markup.add(curve_l, curve_m, spec_wide, fixer, effect, remove)
        await message.answer(KYLIE_EFFECT, reply_markup=markup)

    elif message.text == remove_lashes:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        curve_l = types.KeyboardButton(curve_l)
        curve_m = types.KeyboardButton(curve_m)
        spec_wide = types.KeyboardButton(spec_wide)
        fixer = types.KeyboardButton(fixer)
        effect = types.KeyboardButton(kylie_effect)
        remove = types.KeyboardButton(back)
        markup.add(curve_l, curve_m, spec_wide, fixer, effect, remove)
        await message.answer(REMOVE_LASHES, reply_markup=markup)

    else:
        markup = types.InlineKeyboardMarkup(row_width=1)
        instagram = types.InlineKeyboardButton("Мой Instagram 📸", "https://instagram.com/browbarmsk")
        whatsapp = types.InlineKeyboardButton("Мой WhatsApp", url="https://wa.me/79999788423")
        telegram = types.InlineKeyboardButton("Мой Telegram", url="https://t.me/dokbaeva")
        markup.add(instagram, whatsapp, telegram)
        await message.answer("Я не знаю что ты имеешь ввиду🥺\nНо ты можешь написать мне ⬇️", reply_markup=markup)


    
    #await bot.send_message(message.chat.id, message.text)
    #await message.answer(message.text.upper())



#@dp.message_handler(Text(equals="С пюрешкой"))
#async def with_puree(message: types.Message):
#    await message.reply("Отличный выбор!", reply_markup=types.ReplyKeyboardRemove())
#
#@dp.message_handler(lambda message: message.text == "Без пюрешки")
#async def without_puree(message: types.Message):
#    await message.reply("Так невкусно!", reply_markup=types.ReplyKeyboardRemove())

#@dp.message_handler(commands='starts')
#async def send_welcome(message: types.Message):
 #   """
  #  This handler will be called when user sends `/start` or `/help` command
#    """
   # await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")
#    buttons = [
#        types.InlineKeyboardButton(text="GitHub", url="https://github.com"),
#        types.InlineKeyboardButton(text="Оф. канал Telegram", url="tg://resolve?domain=telegram"),
#    ]
#    keyboard = types.InlineKeyboardMarkup(row_width=1)
#    keyboard.add(*buttons)
#    await message.answer("Hi Friend! How can I help you?", reply_markup=keyboard)
#
#@dp.message_handler(commands="starts")
#async def cmd_start(message: types.Message):
#    keyboard = types.ReplyKeyboardMarkup()
#    button_1 = types.KeyboardButton(text="С пюрешкой")
#    keyboard.add(button_1)
#    button_2 = "Без пюрешки"
#    keyboard.add(button_2)
#    await message.answer("Как подавать котлеты?", reply_markup=keyboard)




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
