import telebot

from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton

import config
from markups import *

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def start_func(message):
    bot.send_message(message.chat.id, f'Привет 🤝 {message.from_user.first_name} 🤝 !\n{start_msg}',
                     reply_markup=get_reply_keyboard([info_btn]))


@bot.message_handler(content_types='text')
def main_menu(message):
    answer = message.text
    commands_list = [info_btn, booking_btn, back_btn, price_btn, reviews_btn, kitchen_btn]

    if answer == info_btn:
        bot.send_message(message.chat.id, about_us, reply_markup=get_reply_keyboard([price_btn,
                                                                                     booking_btn,
                                                                                     back_btn, reviews_btn, kitchen_btn]))
    if answer == booking_btn:
        keyboard = InlineKeyboardMarkup()
        url_button = InlineKeyboardButton(text=booking_btn, url="http://goodgame-ufa.herokuapp.com/booking/new")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, f"{booking_msg}\n{booking_btn}.", reply_markup=keyboard)
    if answer == back_btn:
        bot.send_message(message.chat.id, f'Привет 🤝 {message.from_user.first_name} 🤝 !\n{start_msg}',
                         reply_markup=get_reply_keyboard([info_btn]))

    if answer == price_btn:
        #keyboard = InlineKeyboardMarkup()
        #url_button = InlineKeyboardButton(text=price_btn, url="https://telegra.ph/Nash-prajs-06-12-2")
        #keyboard.add(url_button)
        #bot.send_message(message.chat.id, f"{price_msg}\n{price_btn}.", reply_markup=keyboard)
        bot.send_photo(message.chat.id, photo=open('img/game_menu.jpg', 'rb'))

    if answer == reviews_btn:
        keyboard = InlineKeyboardMarkup()
        url_button = InlineKeyboardButton(text=reviews_btn, url="https://forms.gle/zmLoxGQoKz8bnqVx6")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, f"{reviews_msg}\n{reviews_btn}.", reply_markup=keyboard)

    if answer == kitchen_btn:
        #keyboard = InlineKeyboardMarkup()
        #url_button = InlineKeyboardButton(text=kitchen_btn, url="https://telegra.ph/Menyu-kuhni-06-23")
        #keyboard.add(url_button)
        #bot.send_message(message.chat.id, f"{kitchen_msg}.", reply_markup=keyboard)
        bot.send_photo(message.chat.id, photo=open("img/menu_kitchen1.jpg", "rb"))
        bot.send_photo(message.chat.id, open("img/menu_kitchen2.jpg", "rb"))

    if answer not in commands_list:
        bot.send_message(message.chat.id, error_msg)
        bot.send_message(message.chat.id, f'Привет 🤝 {message.from_user.first_name} 🤝 !\n{start_msg}',
                         reply_markup=get_reply_keyboard([info_btn]))


if __name__ == "__main__":
    bot.polling(none_stop=True)
