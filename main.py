import sqlite3
import telebot
from telebot import types

bot = telebot.TeleBot('5844454094:AAHygFGw3mZRQywtTrpw4_jxSs8GH79sies')
@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🛒 Сделать заказ")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "Здравствуйте, готовы сделать заказ?", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):


    if message.text == '🛒 Сделать заказ' :
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🍓 Плодово-ягодные")
        btn2 = types.KeyboardButton('🌸 Декоративные')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, "👋 Вас приветствует бот магазина Новый садовник", reply_markup=markup)
        bot.send_message(message.from_user.id, '👀 Выберите интересующий вас раздел')

    elif message.text == '🍓 Плодово-ягодные':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🍑 Абрикос')
        btn2 = types.KeyboardButton('🍠 Боярышник')
        btn3 = types.KeyboardButton('🍇 Виноград')
        btn4 = types.KeyboardButton('🍒🟪 Вишне-Черешня')
        btn5 = types.KeyboardButton('🍒 Вишня')
        btn6 = types.KeyboardButton('🟣 Голубика')
        btn7 = types.KeyboardButton('🍓🌑 Ежевика')
        btn8 = types.KeyboardButton('🍇🌑 Жимолость')
        btn9 = types.KeyboardButton('🍉 Крыжовник')
        btn10 = types.KeyboardButton('🍓 Малина')
        btn11 = types.KeyboardButton('🥭 Слива')
        btn12 = types.KeyboardButton('🥭 Алыча')
        btn13 = types.KeyboardButton('🌑 Смородина')
        btn14 = types.KeyboardButton('🍒 Клюква')
        btn15 = types.KeyboardButton('🍇🌑 Шелковица')
        btn16 = types.KeyboardButton('🐿️ Грецкий орех')
        btn17 = types.KeyboardButton('🔙 К разделам')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13, btn14, btn15, btn16, btn17)
        bot.send_message(message.from_user.id, '⬇ Выберите подраздел', reply_markup=markup)

    elif message.text == '🔙 К подразделам':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🍑 Абрикос')
        btn2 = types.KeyboardButton('🍠 Боярышник')
        btn3 = types.KeyboardButton('🍇 Виноград')
        btn4 = types.KeyboardButton('🍒🟪 Вишне-Черешня')
        btn5 = types.KeyboardButton('🍒 Вишня')
        btn6 = types.KeyboardButton('🟣 Голубика')
        btn7 = types.KeyboardButton('🍓🌑 Ежевика')
        btn8 = types.KeyboardButton('🍇🌑 Жимолость')
        btn9 = types.KeyboardButton('🍉 Крыжовник')
        btn10 = types.KeyboardButton('🍓 Малина')
        btn11 = types.KeyboardButton('🥭 Слива')
        btn12 = types.KeyboardButton('🥭 Алыча')
        btn13 = types.KeyboardButton('🌑 Смородина')
        btn14 = types.KeyboardButton('🍒 Клюква')
        btn15 = types.KeyboardButton('🍇🌑 Шелковица')
        btn16 = types.KeyboardButton('🐿️ Грецкий орех')
        btn17 = types.KeyboardButton('🔙 К разделам')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13, btn14, btn15, btn16, btn17)
        bot.send_message(message.from_user.id, '⬇ Выберите подраздел', reply_markup=markup)

    elif message.text == '🔙 К разделам' :
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🍓 Плодово-ягодные")
        btn2 = types.KeyboardButton('🌸 Декоративные')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, "👀 Выберите интересующий вас раздел", reply_markup=markup)

    elif message.text == '🍑 Абрикос':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Брянский ранний')
        btn2 = types.KeyboardButton('Орловчанин')
        btn3 = types.KeyboardButton('Чемпион севера')
        btn4 = types.KeyboardButton('Манитоба')
        btn5 = types.KeyboardButton('🔙 К подразделам')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.from_user.id, '⬇ Выберите сорт', reply_markup=markup)

    elif message.text == '🔙 К абрикосам':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Брянский ранний')
        btn2 = types.KeyboardButton('Орловчанин')
        btn3 = types.KeyboardButton('Чемпион севера')
        btn4 = types.KeyboardButton('Манитоба')
        btn5 = types.KeyboardButton('🔙 К подразделам')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.from_user.id, '⬇ Выберите сорт', reply_markup=markup)

    elif message.text == 'Брянский ранний':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К абрикосам')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/a/fSA5spG" )
        bot.send_message(message.from_user.id, 'Стоимость: ', reply_markup=markup)
        bot.send_message(message.from_user.id, 'Количество: ', reply_markup=markup)

    elif message.text == 'Орловчанин':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К абрикосам')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/a/9Q3nb8K")
        bot.send_message(message.from_user.id, 'Стоимость: ', reply_markup=markup)
        bot.send_message(message.from_user.id, 'Количество: ', reply_markup=markup)

    elif message.text == 'Чемпион севера':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К абрикосам')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/a/IeNiHHn")
        bot.send_message(message.from_user.id, 'Стоимость: ', reply_markup=markup)
        bot.send_message(message.from_user.id, 'Количество: ', reply_markup=markup)

    elif message.text == 'Манитоба':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К абрикосам')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/a/1hAmRNb")
        bot.send_message(message.from_user.id, 'Стоимость: ', reply_markup=markup)
        bot.send_message(message.from_user.id, 'Количество: ', reply_markup=markup)


    elif message.text == '🍠 Боярышник':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Крупноплодный')
        btn2 = types.KeyboardButton('🔙 К подразделам')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, '⬇ Выберите сорт', reply_markup=markup)

    elif message.text == '🔙 К Боярышнику':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Крупноплодный')
        btn2 = types.KeyboardButton('🔙 К подразделам')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, '⬇ Выберите сорт', reply_markup=markup)

    elif message.text == 'Крупноплодный':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Боярышнику')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/a/WVvxBAn")
        bot.send_message(message.from_user.id, 'Стоимость: ', reply_markup=markup)
        bot.send_message(message.from_user.id, 'Количество: ', reply_markup=markup)

    elif message.text == '🍇 Виноград':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Сеня')
        btn2 = types.KeyboardButton('Альфа')
        btn3 = types.KeyboardButton('Бианка')
        btn4 = types.KeyboardButton('Лора')
        btn5 = types.KeyboardButton('🔙 К подразделам')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.from_user.id, '⬇ Выберите сорт', reply_markup=markup)

    elif message.text == '🔙 К Винограду':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Сеня')
        btn2 = types.KeyboardButton('Альфа')
        btn3 = types.KeyboardButton('Бианка')
        btn4 = types.KeyboardButton('Лора')
        btn5 = types.KeyboardButton('🔙 К подразделам')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.from_user.id, '⬇ Выберите сорт', reply_markup=markup)

    elif message.text == 'Сеня':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Винограду')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/a/47C1Yln")
        bot.send_message(message.from_user.id, 'Стоимость: ', reply_markup=markup)
        bot.send_message(message.from_user.id, 'Количество: ', reply_markup=markup)

    elif message.text == 'Альфа':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Винограду')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/a/i32RqzJ")
        bot.send_message(message.from_user.id, 'Стоимость: ', reply_markup=markup)
        bot.send_message(message.from_user.id, 'Количество: ', reply_markup=markup)

    elif message.text == 'Бианка':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Винограду')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/a/14I0BLu")
        bot.send_message(message.from_user.id, 'Стоимость: ', reply_markup=markup)
        bot.send_message(message.from_user.id, 'Количество: ', reply_markup=markup)

    elif message.text == 'Лора':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Винограду')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/a/BxMrNnV")
        bot.send_message(message.from_user.id, 'Стоимость: ', reply_markup=markup)
        bot.send_message(message.from_user.id, 'Количество: ', reply_markup=markup)

    elif message.text == '🍒🟪 Вишне-Черешня':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Спартанка')
        btn2 = types.KeyboardButton('Ночка')
        btn3 = types.KeyboardButton('Надежда')
        btn4 = types.KeyboardButton('Ивановна')
        btn5 = types.KeyboardButton('🔙 К подразделам')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.from_user.id, '⬇ Выберите сорт', reply_markup=markup)

    elif message.text == '🔙 К Вишне-Черешне':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Спартанка')
        btn2 = types.KeyboardButton('Ночка')
        btn3 = types.KeyboardButton('Надежда')
        btn4 = types.KeyboardButton('Ивановна')
        btn5 = types.KeyboardButton('🔙 К подразделам')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.from_user.id, '⬇ Выберите сорт', reply_markup=markup)

    elif message.text == 'Спартанка':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Вишне-Черешне')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/mB63BmU")
        bot.send_message(message.from_user.id, 'Стоимость: ', reply_markup=markup)
        bot.send_message(message.from_user.id, 'Количество: ', reply_markup=markup)

    elif message.text == 'Ночка':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Вишне-Черешне')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/1AbMKCG")
        bot.send_message(message.from_user.id, 'Стоимость: ', reply_markup=markup)
        bot.send_message(message.from_user.id, 'Количество: ', reply_markup=markup)

    elif message.text == 'Надежда':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Вишне-Черешне')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/QZsJLOI")
        bot.send_message(message.from_user.id, 'Стоимость: ', reply_markup=markup)
        bot.send_message(message.from_user.id, 'Количество: ', reply_markup=markup)

    elif message.text == 'Ивановна':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Вишне-Черешне')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/Etxi1FN")
        bot.send_message(message.from_user.id, 'Стоимость: ', reply_markup=markup)
        bot.send_message(message.from_user.id, 'Количество: ', reply_markup=markup)

    elif message.text == '🍒 Вишня':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Россошанская')
        btn2 = types.KeyboardButton('Апухтинская')
        btn3 = types.KeyboardButton('Саратовская малышка')
        btn4 = types.KeyboardButton('Десертная Морозовой')
        btn5 = types.KeyboardButton('🔙 К подразделам')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.from_user.id, '⬇ Выберите сорт', reply_markup=markup)

    elif message.text == '🔙 К Вишне':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Россошанская')
        btn2 = types.KeyboardButton('Апухтинская')
        btn3 = types.KeyboardButton('Саратовская малышка')
        btn4 = types.KeyboardButton('Десертная Морозовой')
        btn5 = types.KeyboardButton('🔙 К подразделам')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.from_user.id, '⬇ Выберите сорт', reply_markup=markup)

    elif message.text == 'Россошанская':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Вишне')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/TvmkcgI")
        bot.send_message(message.from_user.id, 'Стоимость: ', reply_markup=markup)
        bot.send_message(message.from_user.id, 'Количество: ', reply_markup=markup)

    elif message.text == 'Апухтинская':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Вишне')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/zjgtwxO")
        bot.send_message(message.from_user.id, 'Стоимость: ', reply_markup=markup)
        bot.send_message(message.from_user.id, 'Количество: ', reply_markup=markup)

    elif message.text == 'Саратовская малышка':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Вишне')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/io6vuVc")
        bot.send_message(message.from_user.id, 'Стоимость: ', reply_markup=markup)
        bot.send_message(message.from_user.id, 'Количество: ', reply_markup=markup)

    elif message.text == 'Десертная Морозовой':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Вишне')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/7YpLAzm")
        bot.send_message(message.from_user.id, 'Стоимость: ', reply_markup=markup)
        bot.send_message(message.from_user.id, 'Количество: ', reply_markup=markup)

    elif message.text == '🟣 Голубика':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Патриот')
        btn2 = types.KeyboardButton('Нортлэнд')
        btn3 = types.KeyboardButton('Бонус')
        btn4 = types.KeyboardButton('Блюголд')
        btn5 = types.KeyboardButton('🔙 К подразделам')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.from_user.id, '⬇ Выберите сорт', reply_markup=markup)

    elif message.text == '🔙 К Голубике':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Патриот')
        btn2 = types.KeyboardButton('Нортлэнд')
        btn3 = types.KeyboardButton('Бонус')
        btn4 = types.KeyboardButton('Блюголд')
        btn5 = types.KeyboardButton('🔙 К подразделам')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.from_user.id, '⬇ Выберите сорт', reply_markup=markup)

    elif message.text == 'Патриот':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Голубике')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/A5bJWSz")
        bot.send_message(message.from_user.id, 'Стоимость: ', reply_markup=markup)
        bot.send_message(message.from_user.id, 'Количество: ', reply_markup=markup)

    elif message.text == 'Нортлэнд':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Голубике')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/duCbinN")
        bot.send_message(message.from_user.id, 'Стоимость: ', reply_markup=markup)
        bot.send_message(message.from_user.id, 'Количество: ', reply_markup=markup)

    elif message.text == 'Бонус':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Голубике')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/IxYMyLq")
        bot.send_message(message.from_user.id, 'Стоимость: ', reply_markup=markup)
        bot.send_message(message.from_user.id, 'Количество: ', reply_markup=markup)

    elif message.text == 'Блюголд':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Голубике')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/pR34jtY")
        bot.send_message(message.from_user.id, 'Стоимость: ', reply_markup=markup)
        bot.send_message(message.from_user.id, 'Количество: ', reply_markup=markup)

    elif message.text == '🍓🌑 Ежевика':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Честер Торнлесс')
        btn2 = types.KeyboardButton('Натчез')
        btn3 = types.KeyboardButton('Газда')
        btn4 = types.KeyboardButton('Эбони')
        btn5 = types.KeyboardButton('🔙 К подразделам')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.from_user.id, '⬇ Выберите сорт', reply_markup=markup)

    elif message.text == '🔙 К Ежевике':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Честер Торнлесс')
        btn2 = types.KeyboardButton('Натчез')
        btn3 = types.KeyboardButton('Газда')
        btn4 = types.KeyboardButton('Эбони')
        btn5 = types.KeyboardButton('🔙 К подразделам')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.from_user.id, '⬇ Выберите сорт', reply_markup=markup)

    elif message.text == 'Честер Торнлесс':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Ежевике')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/10D0sLb")
        bot.send_message(message.from_user.id, 'Стоимость: ', reply_markup=markup)
        bot.send_message(message.from_user.id, 'Количество: ', reply_markup=markup)

    elif message.text == 'Натчез':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Ежевике')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/YDLB7yd")
        bot.send_message(message.from_user.id, 'Стоимость: ', reply_markup=markup)
        bot.send_message(message.from_user.id, 'Количество: ', reply_markup=markup)

    elif message.text == 'Газда':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Ежевике')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/pbbZeFl")
        bot.send_message(message.from_user.id, 'Стоимость: ', reply_markup=markup)
        bot.send_message(message.from_user.id, 'Количество: ', reply_markup=markup)

    elif message.text == 'Эбони':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Ежевике')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/wAVPXxN")
        bot.send_message(message.from_user.id, 'Стоимость: ', reply_markup=markup)
        bot.send_message(message.from_user.id, 'Количество: ', reply_markup=markup)

    elif message.text == '🍇🌑 Жимолость':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Восторг')
        btn2 = types.KeyboardButton('Бореал Бист')
        btn3 = types.KeyboardButton('Бореал Близзард')
        btn4 = types.KeyboardButton('Индиго Джем')
        btn5 = types.KeyboardButton('🔙 К подразделам')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.from_user.id, '⬇ Выберите сорт', reply_markup=markup)

    elif message.text == '🔙 К Жимолости':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Восторг')
        btn2 = types.KeyboardButton('Бореал Бист')
        btn3 = types.KeyboardButton('Бореал Близзард')
        btn4 = types.KeyboardButton('Индиго Джем')
        btn5 = types.KeyboardButton('🔙 К подразделам')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.from_user.id, '⬇ Выберите сорт', reply_markup=markup)

    elif message.text == 'Восторг':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Жимолости')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/rrl6vTG")
        bot.send_message(message.from_user.id, 'Стоимость: ', reply_markup=markup)
        bot.send_message(message.from_user.id, 'Количество: ', reply_markup=markup)

    elif message.text == 'Бореал Бист':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Жимолости')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/rsy0QHX")
        bot.send_message(message.from_user.id, 'Стоимость: ', reply_markup=markup)
        bot.send_message(message.from_user.id, 'Количество: ', reply_markup=markup)

    elif message.text == 'Бореал Близзард':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Жимолости')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/SNz1yVg")
        bot.send_message(message.from_user.id, 'Стоимость: ', reply_markup=markup)
        bot.send_message(message.from_user.id, 'Количество: ', reply_markup=markup)

    elif message.text == 'Индиго Джем':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Жимолости')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/d9ZrgMq")
        bot.send_message(message.from_user.id, 'Стоимость: ', reply_markup=markup)
        bot.send_message(message.from_user.id, 'Количество: ', reply_markup=markup)

    elif message.text == '🍉 Крыжовник':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Консул')
        btn2 = types.KeyboardButton('Краснославянский')
        btn3 = types.KeyboardButton('🔙 К подразделам')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '⬇ Выберите сорт', reply_markup=markup)

    elif message.text == '🔙 К Крыжовнику':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Консул')
        btn2 = types.KeyboardButton('Краснославянский')
        btn3 = types.KeyboardButton('🔙 К подразделам')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '⬇ Выберите сорт', reply_markup=markup)

    elif message.text == 'Консул':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Крыжовнику')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/cOvRltf")
        bot.send_message(message.from_user.id, 'Стоимость: ', reply_markup=markup)
        bot.send_message(message.from_user.id, 'Количество: ', reply_markup=markup)

    elif message.text == 'Краснославянский':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Крыжовнику')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/OAheIdQ")
        bot.send_message(message.from_user.id, 'Стоимость: ', reply_markup=markup)
        bot.send_message(message.from_user.id, 'Количество: ', reply_markup=markup)

    elif message.text == '🍓 Малина':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Таруса')
        btn2 = types.KeyboardButton('Крепыш')
        btn3 = types.KeyboardButton('Сказка')
        btn4 = types.KeyboardButton('Самородок')
        btn5 = types.KeyboardButton('🔙 К подразделам')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.from_user.id, '⬇ Выберите сорт', reply_markup=markup)

    elif message.text == '🥭 Слива':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Евразия')
        btn2 = types.KeyboardButton('Утро')
        btn3 = types.KeyboardButton('Этюд')
        btn4 = types.KeyboardButton('Ренклод')
        btn5 = types.KeyboardButton('🔙 К подразделам')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.from_user.id, '⬇ Выберите сорт', reply_markup=markup)

    elif message.text == '🥭 Алыча':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Царская')
        btn2 = types.KeyboardButton('Злато скифов')
        btn3 = types.KeyboardButton('Чук')
        btn4 = types.KeyboardButton('🔙 К подразделам')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.from_user.id, '⬇ Выберите сорт', reply_markup=markup)

    elif message.text == '🌑 Смородина':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Загадка')
        btn2 = types.KeyboardButton('Черный жемчуг')
        btn3 = types.KeyboardButton('Пигмей')
        btn4 = types.KeyboardButton('Экзотика')
        btn5 = types.KeyboardButton('🔙 К подразделам')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.from_user.id, '⬇ Выберите сорт', reply_markup=markup)

    elif message.text == '🍒 Клюква':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Бен Лир')
        btn2 = types.KeyboardButton('Макфларин')
        btn3 = types.KeyboardButton('🔙 К подразделам')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '⬇ Выберите сорт', reply_markup=markup)

    elif message.text == '🍇🌑 Шелковица':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Белая')
        btn2 = types.KeyboardButton('Синяя')
        btn3 = types.KeyboardButton('🔙 К подразделам')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '⬇ Выберите сорт', reply_markup=markup)

    elif message.text == '🐿️ Грецкий орех':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Левина')
        btn2 = types.KeyboardButton('Саратовский Идеал')
        btn3 = types.KeyboardButton('🔙 К подразделам')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '⬇ Выберите сорт', reply_markup=markup)

    elif message.text == '🌸 Декоративные':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🌸 Гортензия')
        btn2 = types.KeyboardButton('🌸 Сирень')
        btn3 = types.KeyboardButton('🌸 Спирея')
        btn4 = types.KeyboardButton('🌸 Лапчатка')
        btn5 = types.KeyboardButton('🌸 Чубушник')
        btn6 = types.KeyboardButton('🔙 К разделам')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        bot.send_message(message.from_user.id, '⬇ Выберите подраздел', reply_markup=markup)

    elif message.text == '🔙 К пoдразделам':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🌸 Гортензия')
        btn2 = types.KeyboardButton('🌸 Сирень')
        btn3 = types.KeyboardButton('🌸 Спирея')
        btn4 = types.KeyboardButton('🌸 Лапчатка')
        btn5 = types.KeyboardButton('🌸 Чубушник')
        btn6 = types.KeyboardButton('🔙 К разделам')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        bot.send_message(message.from_user.id, '⬇ Выберите подраздел', reply_markup=markup)

    elif message.text == '🌸 Гортензия':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Тардива')
        btn2 = types.KeyboardButton('Бомбшелл')
        btn3 = types.KeyboardButton('Фантом')
        btn4 = types.KeyboardButton('Сандей фрайз')
        btn5 = types.KeyboardButton('🔙 К пoдразделам')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.from_user.id, '⬇ Выберите сорт', reply_markup=markup)

    elif message.text == '🌸 Сирень':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Галина Уланова')
        btn2 = types.KeyboardButton('Леонид Колесников')
        btn3 = types.KeyboardButton('Невеста')
        btn4 = types.KeyboardButton('Мадам Лемуан')
        btn5 = types.KeyboardButton('🔙 К пoдразделам')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.from_user.id, '⬇ Выберите сорт', reply_markup=markup)

    elif message.text == '🌸 Спирея':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Dars red')
        btn2 = types.KeyboardButton('Gold flame')
        btn3 = types.KeyboardButton('Little Princess')
        btn4 = types.KeyboardButton('Olimpik flaime')
        btn5 = types.KeyboardButton('🔙 К пoдразделам')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.from_user.id, '⬇ Выберите сорт', reply_markup=markup)

    elif message.text == '🌸 Лапчатка':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Голдфингер')
        btn2 = types.KeyboardButton('Маунт Эверест')
        btn3 = types.KeyboardButton('Голд Дрон')
        btn4 = types.KeyboardButton('Примроуз Бьюти')
        btn5 = types.KeyboardButton('🔙 К пoдразделам')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.from_user.id, '⬇ Выберите сорт', reply_markup=markup)

    elif message.text == '🌸 Чубушник':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Сноуболл')
        btn2 = types.KeyboardButton('Комсомолец')
        btn3 = types.KeyboardButton('Глетчер')
        btn4 = types.KeyboardButton('🔙 К пoдразделам')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.from_user.id, '⬇ Выберите сорт', reply_markup=markup)

    elif message.text == 'Сноуболл':
        bot.send_photo(message.from_user.id, "https://imgur.com/a/R4tztsW")
        bot.send_message(message.from_user.id, 'цена: сто тыщ мильонов рублей')



bot.polling(none_stop=True) #обязательная для работы бота часть