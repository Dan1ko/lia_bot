from telebot import types

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('IgM:< 1  IgG:< 10')
btn2 = types.KeyboardButton('IgM:от 1 до 2  IgG:< 10')
btn3 = types.KeyboardButton('IgM:≥ 2 IgG:< 10')
btn4 = types.KeyboardButton('IgM:≥ 2 IgG:≥ 10')
btn5 = types.KeyboardButton('IgM:< 2 IgG:≥ 10')

keyboard.add(btn1, btn2, btn3, btn4, btn5)
