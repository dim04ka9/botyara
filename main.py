import sqlite3
import telebot
from telebot import types
import json

bot = telebot.TeleBot('5844454094:AAHygFGw3mZRQywtTrpw4_jxSs8GH79sies')
ADMIN_ID = 515429348

main_markap = types.ReplyKeyboardMarkup(resize_keyboard=True).add(
    types.KeyboardButton("🍓 Плодово-ягодные"),
    types.KeyboardButton('🌸 Декоративные'),
    types.KeyboardButton('🧺 Корзина')
)

users_states = {}
MAIN_STATE = 'main'
INPUT_NAME_STATE = 'input_name'
INPUT_DATE_STATE = 'input_date'


@bot.message_handler(commands=['start'])
def start(message):
    users_states[message.from_user.id] = {'state': MAIN_STATE, 'name': ''}
    bot.send_message(message.from_user.id, "👋 Вас приветствует бот магазина Новый садовник \n 👀 Выберите интересующий вас раздел", reply_markup=main_markap)


@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    con = sqlite3.connect("db.sqlite")
    cur = con.cursor()

    if call.data == 'order':
        if not users_states.get(call.message.chat.id):
            users_states[call.message.chat.id] = {'state': MAIN_STATE, 'name': ''}
        users_states[call.message.chat.id]['state'] = INPUT_NAME_STATE
        bot.send_message(call.message.chat.id, 'Введите имя:', reply_markup=types.ReplyKeyboardRemove())

    elif call.data == 'clear-basket':
        cur.execute(f"DELETE FROM basket where user_id = '{call.message.chat.id}'")
        con.commit()
        bot.send_message(call.message.chat.id, '✅ Корзина очищена')

    elif call.data.split('--')[1] == 'basket':
        count = cur.execute(f"select count from products where name = '{call.data.split('--')[0]}'").fetchone()
        print()
        markup = types.InlineKeyboardMarkup()
        if count[0] > 0:
            for i in range(count[0]):
                markup.add(
                    types.InlineKeyboardButton(f'{i + 1}', callback_data=f'{call.data.split("--")[0]}--count--{i + 1}'))

            bot.send_message(call.message.chat.id, 'Скока?', reply_markup=markup)
        else:
            bot.send_message(call.message.chat.id, 'Товар закончился, приходите позже')


    elif call.data.split('--')[1] == 'count':
        cur.execute(
            f"INSERT INTO basket (user_id, product_name, count) VALUES ('{call.message.chat.id}', '{call.data.split('--')[0]}', '{call.data.split('--')[2]}');")
        con.commit()
        bot.send_message(call.message.chat.id,
                         f'Добавлено в корзину: {call.data.split("--")[0]} {call.data.split("--")[2]} шт.')

    con.close()


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    con = sqlite3.connect("db.sqlite")
    cur = con.cursor()

    if not users_states.get(message.from_user.id):
        users_states[message.from_user.id] = {'state': MAIN_STATE, 'name': ''}

    if users_states[message.from_user.id]['state'] == INPUT_NAME_STATE:
        users_states[message.from_user.id]['name'] = message.text
        users_states[message.from_user.id]['state'] = INPUT_DATE_STATE
        bot.send_message(message.from_user.id, 'Введите дату:')

    elif users_states[message.from_user.id]['state'] == INPUT_DATE_STATE:
        users_states[message.from_user.id]['state'] = MAIN_STATE
        date = message.text
        name = users_states[message.from_user.id]['name']

        rows = cur.execute(
            f"select * from basket INNER JOIN products ON name = product_name where user_id = '{message.from_user.id}'").fetchall()

        if len(rows):
            msg = 'Заказ:\n\n'
            msg += f'Имя: {name}\n'
            msg += f'Дата: {date}\n\n'
            msg += 'Название \t|\t Кол-во \t|\t Цена \n\n'
            summa = 0
            content = []
            for row in rows:
                count = 0
                if row[6] - row[3] > 0:
                    count = row[6] - row[3]
                cur.execute(
                    f"UPDATE products SET count = {count} where name = '{row[2]}';")
                con.commit()

                content.append({
                    'product_name': row[2],
                    'count': row[3]
                })
                msg += f'{row[2]} \t|\t {row[3]} \t|\t {row[8]}\n'
                summa += row[3] * row[8]

            msg += f'\nСумма заказа: {summa} рублей'

            bot.send_message(ADMIN_ID, msg)

            cur.execute(
                f"INSERT INTO orders (name, date, summa, content) VALUES ('{name}', '{date}', '{summa}', '{json.dumps(content, ensure_ascii=False,)}');")
            con.commit()

            bot.send_message(message.from_user.id, 'Заказ оформлен', reply_markup=main_markap)

            cur.execute(f"DELETE FROM basket where user_id = '{message.from_user.id}'")
            con.commit()
        else:
            bot.send_message(message.from_user.id, 'Ошибка, корзина пуста', reply_markup=main_markap)


    elif message.text == '🧺 Корзина':
        rows = cur.execute(f"select * from basket INNER JOIN products ON name = product_name where user_id = '{message.from_user.id}'").fetchall()

        if len(rows):
            msg = 'Корзина:\n\n'
            msg += 'Название \t|\t Кол-во \t|\t Цена \n\n'
            summa = 0
            for row in rows:
                msg += f'{row[2]} \t|\t {row[3]} \t|\t {row[8]}\n'
                summa += row[3] * row[8]

            msg += f'\nСумма заказа: {summa} рублей'

            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('🛒 Сделать заказ', callback_data='order'))
            markup.add(types.InlineKeyboardButton('♻ Очистить корзину', callback_data='clear-basket'))
            bot.send_message(message.from_user.id, msg, reply_markup=markup)
        else:
            bot.send_message(message.from_user.id, 'Корзина пуста')




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
        bot.send_message(message.from_user.id, "👀 Выберите интересующий вас раздел", reply_markup=main_markap)

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
        bot.send_photo(message.from_user.id, "https://imgur.com/a/fSA5spG")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🛒 В корзину', callback_data=f'{message.text}--basket'))
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей \n Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Орловчанин':

        bot.send_photo(message.from_user.id, "https://imgur.com/a/9Q3nb8K")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🛒 В корзину', callback_data=f'{message.text}--basket'))
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей \n Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Чемпион севера':

        bot.send_photo(message.from_user.id, "https://imgur.com/a/IeNiHHn")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🛒 В корзину', callback_data=f'{message.text}--basket'))
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей \n Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Манитоба':

        bot.send_photo(message.from_user.id, "https://imgur.com/a/1hAmRNb")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🛒 В корзину', callback_data=f'{message.text}--basket'))
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей \n Количество: {product[2]} штук', reply_markup=markup)

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

        bot.send_photo(message.from_user.id, "https://imgur.com/a/WVvxBAn")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🛒 В корзину', callback_data=f'{message.text}--basket'))
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей \n Количество: {product[2]} штук', reply_markup=markup)

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

        bot.send_photo(message.from_user.id, "https://imgur.com/a/47C1Yln")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🛒 В корзину', callback_data=f'{message.text}--basket'))
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей \n Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Альфа':

        bot.send_photo(message.from_user.id, "https://imgur.com/a/i32RqzJ")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🛒 В корзину', callback_data=f'{message.text}--basket'))
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей \n Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Бианка':

        bot.send_photo(message.from_user.id, "https://imgur.com/a/14I0BLu")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🛒 В корзину', callback_data=f'{message.text}--basket'))
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей \n Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Лора':

        bot.send_photo(message.from_user.id, "https://imgur.com/a/BxMrNnV")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🛒 В корзину', callback_data=f'{message.text}--basket'))
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей \n Количество: {product[2]} штук', reply_markup=markup)

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

        bot.send_photo(message.from_user.id, "https://imgur.com/mB63BmU")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🛒 В корзину', callback_data=f'{message.text}--basket'))
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей \n Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Ночка':

        bot.send_photo(message.from_user.id, "https://imgur.com/1AbMKCG")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🛒 В корзину', callback_data=f'{message.text}--basket'))
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей \n Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Надежда':

        bot.send_photo(message.from_user.id, "https://imgur.com/QZsJLOI")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🛒 В корзину', callback_data=f'{message.text}--basket'))
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей \n Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Ивановна':

        bot.send_photo(message.from_user.id, "https://imgur.com/Etxi1FN")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🛒 В корзину', callback_data=f'{message.text}--basket'))
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей \n Количество: {product[2]} штук', reply_markup=markup)

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

        bot.send_photo(message.from_user.id, "https://imgur.com/TvmkcgI")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🛒 В корзину', callback_data=f'{message.text}--basket'))
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей \n Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Апухтинская':

        bot.send_photo(message.from_user.id, "https://imgur.com/zjgtwxO")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🛒 В корзину', callback_data=f'{message.text}--basket'))
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей \n Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Саратовская малышка':

        bot.send_photo(message.from_user.id, "https://imgur.com/io6vuVc")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🛒 В корзину', callback_data=f'{message.text}--basket'))
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей \n Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Десертная Морозовой':

        bot.send_photo(message.from_user.id, "https://imgur.com/7YpLAzm")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🛒 В корзину', callback_data=f'{message.text}--basket'))
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей \n Количество: {product[2]} штук', reply_markup=markup)

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

        bot.send_photo(message.from_user.id, "https://imgur.com/A5bJWSz")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🛒 В корзину', callback_data=f'{message.text}--basket'))
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей \n Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Нортлэнд':

        bot.send_photo(message.from_user.id, "https://imgur.com/duCbinN")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🛒 В корзину', callback_data=f'{message.text}--basket'))
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей \n Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Бонус':

        bot.send_photo(message.from_user.id, "https://imgur.com/IxYMyLq")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🛒 В корзину', callback_data=f'{message.text}--basket'))
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей \n Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Блюголд':

        bot.send_photo(message.from_user.id, "https://imgur.com/pR34jtY")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🛒 В корзину', callback_data=f'{message.text}--basket'))
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей \n Количество: {product[2]} штук', reply_markup=markup)

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

        bot.send_photo(message.from_user.id, "https://imgur.com/10D0sLb")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🛒 В корзину', callback_data=f'{message.text}--basket'))
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей \n Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Натчез':

        bot.send_photo(message.from_user.id, "https://imgur.com/YDLB7yd")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🛒 В корзину', callback_data=f'{message.text}--basket'))
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей \n Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Газда':

        bot.send_photo(message.from_user.id, "https://imgur.com/pbbZeFl")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🛒 В корзину', callback_data=f'{message.text}--basket'))
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей \n Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Эбони':

        bot.send_photo(message.from_user.id, "https://imgur.com/wAVPXxN")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🛒 В корзину', callback_data=f'{message.text}--basket'))
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей \n Количество: {product[2]} штук', reply_markup=markup)

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

        bot.send_photo(message.from_user.id, "https://imgur.com/rrl6vTG")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🛒 В корзину', callback_data=f'{message.text}--basket'))
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей \n Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Бореал Бист':

        bot.send_photo(message.from_user.id, "https://imgur.com/rsy0QHX")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🛒 В корзину', callback_data=f'{message.text}--basket'))
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей \n Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Бореал Близзард':

        bot.send_photo(message.from_user.id, "https://imgur.com/SNz1yVg")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🛒 В корзину', callback_data=f'{message.text}--basket'))
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей \n Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Индиго Джем':

        bot.send_photo(message.from_user.id, "https://imgur.com/d9ZrgMq")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🛒 В корзину', callback_data=f'{message.text}--basket'))
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей \n Количество: {product[2]} штук', reply_markup=markup)

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

        bot.send_photo(message.from_user.id, "https://imgur.com/cOvRltf")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🛒 В корзину', callback_data=f'{message.text}--basket'))
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей \n Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Краснославянский':

        bot.send_photo(message.from_user.id, "https://imgur.com/OAheIdQ")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🛒 В корзину', callback_data=f'{message.text}--basket'))
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей \n Количество: {product[2]} штук', reply_markup=markup)

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

        bot.send_photo(message.from_user.id, "https://imgur.com/a/drAc1I2")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🛒 В корзину', callback_data=f'{message.text}--basket'))
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей \n Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Крепыш':

        bot.send_photo(message.from_user.id, "https://imgur.com/6KH0lmK")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🛒 В корзину', callback_data=f'{message.text}--basket'))
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей \n Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Сказка':

        bot.send_photo(message.from_user.id, "https://imgur.com/gwa8F0k")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🛒 В корзину', callback_data=f'{message.text}--basket'))
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей \n Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Самородок':

        bot.send_photo(message.from_user.id, "https://imgur.com/5XNja6t")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🛒 В корзину', callback_data=f'{message.text}--basket'))
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей \n Количество: {product[2]} штук', reply_markup=markup)

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

        bot.send_photo(message.from_user.id, "https://imgur.com/6gbGs4P")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🛒 В корзину', callback_data=f'{message.text}--basket'))
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей \n Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Утро':

        bot.send_photo(message.from_user.id, "https://imgur.com/XgA80OX")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🛒 В корзину', callback_data=f'{message.text}--basket'))
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей \n Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Этюд':

        bot.send_photo(message.from_user.id, "https://imgur.com/FlDXnRb")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🛒 В корзину', callback_data=f'{message.text}--basket'))
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей \n Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Ренклод':

        bot.send_photo(message.from_user.id, "https://imgur.com/lWTKhRj")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🛒 В корзину', callback_data=f'{message.text}--basket'))
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей \n Количество: {product[2]} штук', reply_markup=markup)

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

        bot.send_photo(message.from_user.id, "https://imgur.com/L131nJm")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🛒 В корзину', callback_data=f'{message.text}--basket'))
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей \n Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Злато скифов':

        bot.send_photo(message.from_user.id, "https://imgur.com/S0WJNDg")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🛒 В корзину', callback_data=f'{message.text}--basket'))
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей \n Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Чук':

        bot.send_photo(message.from_user.id, "https://imgur.com/0JGftOb")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🛒 В корзину', callback_data=f'{message.text}--basket'))
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей \n Количество: {product[2]} штук', reply_markup=markup)

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

        bot.send_photo(message.from_user.id, "https://imgur.com/7l8bduF")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🛒 В корзину', callback_data=f'{message.text}--basket'))
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей \n Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Черный жемчуг':

        bot.send_photo(message.from_user.id, "https://imgur.com/D4HvjHG")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🛒 В корзину', callback_data=f'{message.text}--basket'))
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей \n Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Пигмей':

        bot.send_photo(message.from_user.id, "https://imgur.com/RN4HV7l")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🛒 В корзину', callback_data=f'{message.text}--basket'))
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей \n Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Экзотика':

        bot.send_photo(message.from_user.id, "https://imgur.com/pUcbF0m")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🛒 В корзину', callback_data=f'{message.text}--basket'))
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей \n Количество: {product[2]} штук', reply_markup=markup)

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

        bot.send_photo(message.from_user.id, "https://imgur.com/9BsILfE")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🛒 В корзину', callback_data=f'{message.text}--basket'))
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей \n Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Макфларин':

        bot.send_photo(message.from_user.id, "https://imgur.com/ZXr4kuZ")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🛒 В корзину', callback_data=f'{message.text}--basket'))
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей \n Количество: {product[2]} штук', reply_markup=markup)

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

        bot.send_photo(message.from_user.id, "https://imgur.com/N9n8lLU")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🛒 В корзину', callback_data=f'{message.text}--basket'))
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей \n Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Синяя':

        bot.send_photo(message.from_user.id, "https://imgur.com/JadMSl3")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🛒 В корзину', callback_data=f'{message.text}--basket'))
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей \n Количество: {product[2]} штук', reply_markup=markup)

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

        bot.send_photo(message.from_user.id, "https://imgur.com/7CdITwW")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🛒 В корзину', callback_data=f'{message.text}--basket'))
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей \n Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Саратовский Идеал':

        bot.send_photo(message.from_user.id, "https://imgur.com/ke29HKp")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🛒 В корзину', callback_data=f'{message.text}--basket'))
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей \n Количество: {product[2]} штук', reply_markup=markup)

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

        bot.send_photo(message.from_user.id, "https://imgur.com/HlIznLs")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🛒 В корзину', callback_data=f'{message.text}--basket'))
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей \n Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Бомбшелл':

        bot.send_photo(message.from_user.id, "https://imgur.com/eVlI0Jb")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🛒 В корзину', callback_data=f'{message.text}--basket'))
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей \n Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Фантом':

        bot.send_photo(message.from_user.id, "https://imgur.com/LKzYsVM")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🛒 В корзину', callback_data=f'{message.text}--basket'))
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей \n Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Сандей фрайз':

        bot.send_photo(message.from_user.id, "https://imgur.com/wHW13Yl")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🛒 В корзину', callback_data=f'{message.text}--basket'))
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей \n Количество: {product[2]} штук', reply_markup=markup)

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

        bot.send_photo(message.from_user.id, "https://imgur.com/a/WN24Qno")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🛒 В корзину', callback_data=f'{message.text}--basket'))
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей \n Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Леонид Колесников':

        bot.send_photo(message.from_user.id, "https://imgur.com/rHVyi6T")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🛒 В корзину', callback_data=f'{message.text}--basket'))
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей \n Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Невеста':

        bot.send_photo(message.from_user.id, "https://imgur.com/1TdjDqu")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🛒 В корзину', callback_data=f'{message.text}--basket'))
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей \n Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Мадам Лемуан':

        bot.send_photo(message.from_user.id, "https://imgur.com/MmPWy4v")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🛒 В корзину', callback_data=f'{message.text}--basket'))
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей \n Количество: {product[2]} штук', reply_markup=markup)

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

        bot.send_photo(message.from_user.id, "https://imgur.com/kNjIDAP")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🛒 В корзину', callback_data=f'{message.text}--basket'))
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей \n Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Gold flame':

        bot.send_photo(message.from_user.id, "https://imgur.com/tPQ9291")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🛒 В корзину', callback_data=f'{message.text}--basket'))
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей \n Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Little Princess':

        bot.send_photo(message.from_user.id, "https://imgur.com/tmO9r2L")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🛒 В корзину', callback_data=f'{message.text}--basket'))
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей \n Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Olimpik flaime':

        bot.send_photo(message.from_user.id, "https://imgur.com/BnMKfWR")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🛒 В корзину', callback_data=f'{message.text}--basket'))
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей \n Количество: {product[2]} штук', reply_markup=markup)

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

        bot.send_photo(message.from_user.id, "https://imgur.com/hJkKIq2")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🛒 В корзину', callback_data=f'{message.text}--basket'))
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей \n Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Маунт Эверест':

        bot.send_photo(message.from_user.id, "https://imgur.com/8WgrqS8")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🛒 В корзину', callback_data=f'{message.text}--basket'))
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей \n Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Голд Дрон':

        bot.send_photo(message.from_user.id, "https://imgur.com/jKWv4tm")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🛒 В корзину', callback_data=f'{message.text}--basket'))
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей \n Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Примроуз Бьюти':

        bot.send_photo(message.from_user.id, "https://imgur.com/oqQyVIk")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🛒 В корзину', callback_data=f'{message.text}--basket'))
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей \n Количество: {product[2]} штук', reply_markup=markup)

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

        bot.send_photo(message.from_user.id, "https://imgur.com/Ao2qOEQ")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🛒 В корзину', callback_data=f'{message.text}--basket'))
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей \n Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Комсомолец':

        bot.send_photo(message.from_user.id, "https://imgur.com/TL70vjw")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🛒 В корзину', callback_data=f'{message.text}--basket'))
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей \n Количество: {product[2]} штук', reply_markup=markup)

    elif message.text == 'Глетчер':

        bot.send_photo(message.from_user.id, "https://imgur.com/DlXIjNr")
        product = cur.execute(f"SELECT * FROM products WHERE name = '{message.text}'").fetchone()
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🛒 В корзину', callback_data=f'{message.text}--basket'))
        bot.send_message(message.from_user.id, f'Стоимость: {product[4]} рублей \n Количество: {product[2]} штук', reply_markup=markup)

    con.close()



bot.polling(none_stop=True)  # обязательная для работы бота часть