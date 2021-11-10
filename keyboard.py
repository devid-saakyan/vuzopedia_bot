from aiogram import types

def keyboard1():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button1 = types.KeyboardButton('Да')
    button2 = types.KeyboardButton('Нет')
    markup.add(button1,button2)
    return markup

def keyboard2():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button1 = types.KeyboardButton('Платная основа')
    button2 = types.KeyboardButton('Бюджет')
    markup.add(button1,button2)
    return markup

def keyboard3():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button1 = types.KeyboardButton('Очная')
    button2 = types.KeyboardButton('Очно-заочная')
    button3 = types.KeyboardButton('Заочная')
    markup.add(button1,button2,button3)
    return markup
