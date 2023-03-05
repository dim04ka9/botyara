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

categories_markap = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton("🍓 Плодово-ягодные")
btn2 = types.KeyboardButton('🌸 Декоративные')
categories_markap.add(btn1, btn2)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # Подключение к БД
    con = sqlite3.connect("db.sqlite")
    # Создание курсора
    cur = con.cursor()

    if message.text == '🛒 Сделать заказ':
        bot.send_message(message.from_user.id, "👋 Вас приветствует бот магазина Новый садовник", reply_markup=categories_markap)
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
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13, btn14, btn15,
                   btn16, btn17)
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
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13, btn14, btn15,
                   btn16, btn17)
        bot.send_message(message.from_user.id, '⬇ Выберите подраздел', reply_markup=markup)

    elif message.text == '🔙 К разделам':
        bot.send_message(message.from_user.id, "👀 Выберите интересующий вас раздел", reply_markup=categories_markap)

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
        bot.send_photo(message.from_user.id, "https://imgur.com/a/fSA5spG")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Орловчанин':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К абрикосам')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/a/9Q3nb8K")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Чемпион севера':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К абрикосам')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/a/IeNiHHn")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Манитоба':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К абрикосам')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/a/1hAmRNb")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Количество: {product[2]} штук', reply_markup=markup)

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
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Количество: {product[2]} штук', reply_markup=markup)

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
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Альфа':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Винограду')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/a/i32RqzJ")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Бианка':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Винограду')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/a/14I0BLu")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Лора':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Винограду')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/a/BxMrNnV")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Количество: {product[2]} штук', reply_markup=markup)

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
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Ночка':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Вишне-Черешне')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/1AbMKCG")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Надежда':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Вишне-Черешне')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/QZsJLOI")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Ивановна':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Вишне-Черешне')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/Etxi1FN")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Количество: {product[2]} штук', reply_markup=markup)

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
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Апухтинская':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Вишне')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/zjgtwxO")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Саратовская малышка':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Вишне')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/io6vuVc")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Десертная Морозовой':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Вишне')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/7YpLAzm")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Количество: {product[2]} штук', reply_markup=markup)

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
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Нортлэнд':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Голубике')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/duCbinN")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Бонус':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Голубике')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/IxYMyLq")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Блюголд':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Голубике')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/pR34jtY")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Количество: {product[2]} штук', reply_markup=markup)

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
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Натчез':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Ежевике')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/YDLB7yd")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Газда':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Ежевике')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/pbbZeFl")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Эбони':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Ежевике')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/wAVPXxN")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Количество: {product[2]} штук', reply_markup=markup)

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
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Бореал Бист':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Жимолости')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/rsy0QHX")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Бореал Близзард':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Жимолости')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/SNz1yVg")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Индиго Джем':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Жимолости')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/d9ZrgMq")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Количество: {product[2]} штук', reply_markup=markup)

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
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Краснославянский':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Крыжовнику')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/OAheIdQ")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == '🍓 Малина':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Таруса')
        btn2 = types.KeyboardButton('Крепыш')
        btn3 = types.KeyboardButton('Сказка')
        btn4 = types.KeyboardButton('Самородок')
        btn5 = types.KeyboardButton('🔙 К подразделам')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.from_user.id, '⬇ Выберите сорт', reply_markup=markup)

    elif message.text == '🔙 К Малине':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Таруса')
        btn2 = types.KeyboardButton('Крепыш')
        btn3 = types.KeyboardButton('Сказка')
        btn4 = types.KeyboardButton('Самородок')
        btn5 = types.KeyboardButton('🔙 К подразделам')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.from_user.id, '⬇ Выберите сорт', reply_markup=markup)

    elif message.text == 'Таруса':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Малине')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/a/drAc1I2")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Крепыш':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Малине')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/6KH0lmK")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Сказка':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Малине')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/gwa8F0k")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Самородок':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Малине')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/5XNja6t")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == '🥭 Слива':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Евразия')
        btn2 = types.KeyboardButton('Утро')
        btn3 = types.KeyboardButton('Этюд')
        btn4 = types.KeyboardButton('Ренклод')
        btn5 = types.KeyboardButton('🔙 К подразделам')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.from_user.id, '⬇ Выберите сорт', reply_markup=markup)

    elif message.text == '🔙 К Сливе':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Евразия')
        btn2 = types.KeyboardButton('Утро')
        btn3 = types.KeyboardButton('Этюд')
        btn4 = types.KeyboardButton('Ренклод')
        btn5 = types.KeyboardButton('🔙 К подразделам')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.from_user.id, '⬇ Выберите сорт', reply_markup=markup)

    elif message.text == 'Евразия':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Сливе')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/6gbGs4P")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Утро':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Сливе')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/XgA80OX")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Этюд':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Сливе')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/FlDXnRb")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Ренклод':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Сливе')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/lWTKhRj")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == '🥭 Алыча':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Царская')
        btn2 = types.KeyboardButton('Злато скифов')
        btn3 = types.KeyboardButton('Чук')
        btn4 = types.KeyboardButton('🔙 К подразделам')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.from_user.id, '⬇ Выберите сорт', reply_markup=markup)

    elif message.text == '🔙 К Алыче':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Царская')
        btn2 = types.KeyboardButton('Злато скифов')
        btn3 = types.KeyboardButton('Чук')
        btn4 = types.KeyboardButton('🔙 К подразделам')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.from_user.id, '⬇ Выберите сорт', reply_markup=markup)

    elif message.text == 'Царская':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Алыче')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/L131nJm")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Злато скифов':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Алыче')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/S0WJNDg")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Чук':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Алыче')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/0JGftOb")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == '🌑 Смородина':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Загадка')
        btn2 = types.KeyboardButton('Черный жемчуг')
        btn3 = types.KeyboardButton('Пигмей')
        btn4 = types.KeyboardButton('Экзотика')
        btn5 = types.KeyboardButton('🔙 К подразделам')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.from_user.id, '⬇ Выберите сорт', reply_markup=markup)

    elif message.text == '🔙 К Смородине':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Загадка')
        btn2 = types.KeyboardButton('Черный жемчуг')
        btn3 = types.KeyboardButton('Пигмей')
        btn4 = types.KeyboardButton('Экзотика')
        btn5 = types.KeyboardButton('🔙 К подразделам')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.from_user.id, '⬇ Выберите сорт', reply_markup=markup)

    elif message.text == 'Загадка':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Смородине')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/7l8bduF")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Черный жемчуг':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Смородине')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/D4HvjHG")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Пигмей':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Смородине')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/RN4HV7l")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Экзотика':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Смородине')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/pUcbF0m")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == '🍒 Клюква':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Бен Лир')
        btn2 = types.KeyboardButton('Макфларин')
        btn3 = types.KeyboardButton('🔙 К подразделам')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '⬇ Выберите сорт', reply_markup=markup)

    elif message.text == '🔙 К Клюкве':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Бен Лир')
        btn2 = types.KeyboardButton('Макфларин')
        btn3 = types.KeyboardButton('🔙 К подразделам')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '⬇ Выберите сорт', reply_markup=markup)

    elif message.text == 'Бен Лир':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Клюкве')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/9BsILfE")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Макфларин':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Клюкве')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/ZXr4kuZ")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == '🍇🌑 Шелковица':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Белая')
        btn2 = types.KeyboardButton('Синяя')
        btn3 = types.KeyboardButton('🔙 К подразделам')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '⬇ Выберите сорт', reply_markup=markup)

    elif message.text == '🔙 К Шелковице':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Белая')
        btn2 = types.KeyboardButton('Синяя')
        btn3 = types.KeyboardButton('🔙 К подразделам')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '⬇ Выберите сорт', reply_markup=markup)

    elif message.text == 'Белая':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Шелковице')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/N9n8lLU")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Синяя':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Шелковице')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/JadMSl3")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == '🐿️ Грецкий орех':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Левина')
        btn2 = types.KeyboardButton('Саратовский Идеал')
        btn3 = types.KeyboardButton('🔙 К подразделам')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '⬇ Выберите сорт', reply_markup=markup)

    elif message.text == '🔙 К Орехам':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Левина')
        btn2 = types.KeyboardButton('Саратовский Идеал')
        btn3 = types.KeyboardButton('🔙 К подразделам')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '⬇ Выберите сорт', reply_markup=markup)

    elif message.text == 'Левина':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Орехам')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/7CdITwW")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Саратовский Идеал':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Орехам')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/ke29HKp")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Количество: {product[2]} штук', reply_markup=markup)

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

    elif message.text == '🔙 К Гортензиям':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Тардива')
        btn2 = types.KeyboardButton('Бомбшелл')
        btn3 = types.KeyboardButton('Фантом')
        btn4 = types.KeyboardButton('Сандей фрайз')
        btn5 = types.KeyboardButton('🔙 К пoдразделам')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.from_user.id, '⬇ Выберите сорт', reply_markup=markup)

    elif message.text == 'Тардива':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Гортензиям')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/HlIznLs")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Бомбшелл':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Гортензиям')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/eVlI0Jb")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Фантом':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Гортензиям')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/LKzYsVM")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Сандей фрайз':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Гортензиям')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/wHW13Yl")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == '🌸 Сирень':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Галина Уланова')
        btn2 = types.KeyboardButton('Леонид Колесников')
        btn3 = types.KeyboardButton('Невеста')
        btn4 = types.KeyboardButton('Мадам Лемуан')
        btn5 = types.KeyboardButton('🔙 К пoдразделам')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.from_user.id, '⬇ Выберите сорт', reply_markup=markup)

    elif message.text == '🔙 К Сирени':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Галина Уланова')
        btn2 = types.KeyboardButton('Леонид Колесников')
        btn3 = types.KeyboardButton('Невеста')
        btn4 = types.KeyboardButton('Мадам Лемуан')
        btn5 = types.KeyboardButton('🔙 К пoдразделам')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.from_user.id, '⬇ Выберите сорт', reply_markup=markup)

    elif message.text == 'Галина Уланова':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Сирени')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/a/WN24Qno")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Леонид Колесников':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Сирени')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/rHVyi6T")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Невеста':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Сирени')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/1TdjDqu")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Мадам Лемуан':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Сирени')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/MmPWy4v")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == '🌸 Спирея':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Dars red')
        btn2 = types.KeyboardButton('Gold flame')
        btn3 = types.KeyboardButton('Little Princess')
        btn4 = types.KeyboardButton('Olimpik flaime')
        btn5 = types.KeyboardButton('🔙 К пoдразделам')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.from_user.id, '⬇ Выберите сорт', reply_markup=markup)

    elif message.text == '🔙 К Спирее':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Dars red')
        btn2 = types.KeyboardButton('Gold flame')
        btn3 = types.KeyboardButton('Little Princess')
        btn4 = types.KeyboardButton('Olimpik flaime')
        btn5 = types.KeyboardButton('🔙 К пoдразделам')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.from_user.id, '⬇ Выберите сорт', reply_markup=markup)

    elif message.text == 'Dars red':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Спирее')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/kNjIDAP")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Gold flame':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Спирее')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/tPQ9291")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Little Princess':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Спирее')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/tmO9r2L")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Olimpik flaime':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Спирее')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/BnMKfWR")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == '🌸 Лапчатка':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Голдфингер')
        btn2 = types.KeyboardButton('Маунт Эверест')
        btn3 = types.KeyboardButton('Голд Дрон')
        btn4 = types.KeyboardButton('Примроуз Бьюти')
        btn5 = types.KeyboardButton('🔙 К пoдразделам')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.from_user.id, '⬇ Выберите сорт', reply_markup=markup)

    elif message.text == '🔙 К Лапчатке':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Голдфингер')
        btn2 = types.KeyboardButton('Маунт Эверест')
        btn3 = types.KeyboardButton('Голд Дрон')
        btn4 = types.KeyboardButton('Примроуз Бьюти')
        btn5 = types.KeyboardButton('🔙 К пoдразделам')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.from_user.id, '⬇ Выберите сорт', reply_markup=markup)

    elif message.text == 'Голдфингер':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Лапчатке')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/hJkKIq2")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Маунт Эверест':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Лапчатке')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/8WgrqS8")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Голд Дрон':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Лапчатке')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/jKWv4tm")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Примроуз Бьюти':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Лапчатке')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/oqQyVIk")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == '🌸 Чубушник':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Сноуболл')
        btn2 = types.KeyboardButton('Комсомолец')
        btn3 = types.KeyboardButton('Глетчер')
        btn4 = types.KeyboardButton('🔙 К пoдразделам')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.from_user.id, '⬇ Выберите сорт', reply_markup=markup)

    elif message.text == '🔙 К Чубушнику':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Сноуболл')
        btn2 = types.KeyboardButton('Комсомолец')
        btn3 = types.KeyboardButton('Глетчер')
        btn4 = types.KeyboardButton('🔙 К пoдразделам')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.from_user.id, '⬇ Выберите сорт', reply_markup=markup)

    elif message.text == 'Сноуболл':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Чубушнику')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/Ao2qOEQ")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Комсомолец':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Чубушнику')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/TL70vjw")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Глетчер':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 К Чубушнику')
        btn2 = types.KeyboardButton('🛒 В корзину')
        markup.add(btn1, btn2)
        bot.send_photo(message.from_user.id, "https://imgur.com/DlXIjNr")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей', reply_markup=markup)
        bot.send_message(message.from_user.id, f'Количество: {product[2]} штук', reply_markup=markup)


bot.polling(none_stop=True)  # обязательная для работы бота часть