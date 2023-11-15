
from aiogram import Bot, Dispatcher, types, executor

bot = Bot('6595465798:AAFHybFM3J9rtJJXDiyp-J4v8-QgmHa-n_U')
dp = Dispatcher(bot)

@dp.message_handler(content_types=['photo'])
async def start(message: types.Message):
    #await bot.send_message(message.chat.id, 'Hello')
    #await message.answer('Hello')
    await message.reply('Hello')
    #file=open('./video.mp4', 'rb')
    #await message.answer_video(file)


@dp.message_handler(commands=['inline'])
async def info(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Site', url='https://loveties.ru/'))
    markup.add(types.InlineKeyboardButton('Hello', callback_data='hello'))
    await message.reply('Hello', reply_markup=markup)



@dp.callback_query_handler()
async def callback(call):
    await call.message.answer(call.data)


@dp.message_handler(commands=['reply'])
async def reply(message: types.Message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add(types.KeyboardButton('Site'))
    markup.add(types.KeyboardButton('Website'))
    await message.answer('Hello', reply_markup=markup)




executor.start_polling(dp)


#bot = telebot.TeleBot ('6595465798:AAFHybFM3J9rtJJXDiyp-J4v8-QgmHa-n_U')
#bot.polling(none_stop=True)