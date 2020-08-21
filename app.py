import telebot
from keybord import keyboard
from config import BOT_TOKEN
from info import not_met_virus, doubtful_result1, doubtful_result, stage_of_disease, recovered, lia


bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    name = message.from_user
    botz = bot.get_me()
    bot.send_message(message.chat.id, "Здравствуйте👋  😷, {0.first_name}!\n Выберите наиболее подходящий Вам вариант!.".\
                     format(name, botz), reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, lia)


@bot.message_handler(content_types=['text'])
def stat(message):
    #Статистика
    # if message.chat.type == 'private':
    if message.text == 'IgM:< 1  IgG:< 10':
        bot.send_message(message.chat.id, not_met_virus)
    if message.text == 'IgM:от 1 до 2  IgG:< 10':
        bot.send_message(message.chat.id, doubtful_result)
    if message.text == 'IgM:≥ 2 IgG:< 10':
        bot.send_message(message.chat.id, stage_of_disease)
    if message.text == 'IgM:≥ 2 IgG:≥ 10':
        bot.send_message(message.chat.id, doubtful_result1)
    if message.text == 'IgM:< 2 IgG:≥ 10':
        bot.send_message(message.chat.id, recovered)


if __name__=='__main__':
    bot.polling(none_stop=True)
