import telebot
import webbrowser
from telebot import types
import sqlite3

bot = telebot.TeleBot ('6595465798:AAFHybFM3J9rtJJXDiyp-J4v8-QgmHa-n_U')

markup = types.InlineKeyboardMarkup()
markup.add(types.InlineKeyboardButton('Перейти на сайт', url='https://go-friend-go.narod.ru/'))

@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Перейти на сайт', url='https://go-friend-go.narod.ru/')
    markup.row(btn1)
    btn2=types.InlineKeyboardButton('Удалить фото', callback_data='delete')
    btn3=types.InlineKeyboardButton('Изменить текст', callback_data='edit')
    markup.row(btn2, btn3)
    bot.reply_to(message, 'Что за дерьмо ты скинул?!', reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data=='delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)

    elif callback.data=='edit':
        bot.edit_message_text('И бабку твою тоже ебал', callback.message.chat.id, callback.message.message_id)
@bot.message_handler(commands=['site'])
def site(message):
    webbrowser.open('https://go-friend-go.narod.ru/')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}! Выбери одну из команд:\n/start\n/info\n/site\nИли же скинь мне фото, я оценю его\nИли просто посмотри на этого красавчика')
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Перейти на сайт💻')
    markup.row(btn1)
    btn2=types.KeyboardButton('Удалить фото🌇')
    btn3=types.KeyboardButton('Изменить текст😋')
    markup.row(btn2, btn3)
    file = open('./krasavchik.jpg', 'rb' )
    bot.send_photo(message.chat.id, file, reply_markup=markup)
    #bot.send_message(message.chat.id, 'Пошел нахуй!!!', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)
    

def on_click(message):
    if message.text == 'Перейти на сайт💻':
        webbrowser.open('https://go-friend-go.narod.ru/')
    elif message.text == 'Удалить фото🌇':
        bot.delete_message(message.chat.id, message.message_id - 1)
        bot.send_message(message.chat.id, 'Какое фото? Ты че ебу дал')
    elif message.text == 'Изменить текст😋':
        bot.send_message(message.chat.id, 'Я пока хз почему кнопки такие большие ахахах')



@bot.message_handler(commands=['info'])
def main(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}, я ебал твоб маму')




bot.polling(none_stop=True)

