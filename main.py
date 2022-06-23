import telebot
import random
from telebot import types


bot = telebot.TeleBot('5376280994:AAF4PVa4FD7npr2nksgstKkZPK55FrmMAi0')


@bot.message_handler(commands=['start', 'help'])
def start(message):
    mess = f'<b>{message.from_user.first_name} <u>{message.from_user.last_name}</u> - лох</b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == "Hi":
        bot.send_message(message.chat.id, "И тебе hi", parse_mode='html')
    elif message.text == 'id':
        bot.send_message(message.chat.id, f"Твой ID: {message.from_user.id}", parse_mode='html')
    elif message.text == 'photo':
        photo = open('nadya_dasha.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == 'чт':
        bot.send_message(message.chat.id, "o", parse_mode='html')
    else:
        i_dont_know_phrase = ['Я тебя не понимаю', 'Напиши нормально', "эээээ", "Ты сам понял, что написал?",
                              "Я шпрехен дойч", "Помогите пожалуйста девочке", "Альба лох"]
        bot.send_message(message.chat.id, random.choice(i_dont_know_phrase), parse_mode='html')


@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    photo_phrases = ['Мило', "Че по моське", "А ты красавчик", "Кто фотограф?"]
    bot.send_message(message.chat.id, random.choice(photo_phrases))


# @bot.message_handler(commands=['website'])
# def website(message):
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton("чт", url="https://yandex.ru/images/search?text=rfhnbyrb%20%5Bjvzrjd&from=tabbar&pos=11&img_url=https%3A%2F%2Fbelady.online%2Fwp-content%2Fuploads%2F2018%2F08%2Fhomyak-dzhungarik-eda.jpg&rpt=simage&lr=54"))
#     bot.send_message(message.chat.id, 'Перейдите на сайт', reply_markup=markup)


# @bot.message_handler(commands=['website'])
# def website(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#     cho = types.KeyboardButton('чо')
#     cht = types.KeyboardButton('чт')
#     markup.add(cho, cht)
#     bot.send_message(message.chat.id, 'Перейдите на сайт', reply_markup=markup)



bot.polling(none_stop=True)

