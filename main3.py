
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('6595465798:AAFHybFM3J9rtJJXDiyp-J4v8-QgmHa-n_U')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть страницу',web_app=WebAppInfo(url='https://loveties.ru/') ))
    await message.answer('Привет, мой друг!', reply_markup=markup)





executor.start_polling(dp)