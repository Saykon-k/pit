import telebot
import backend_tel as back
bot = telebot.TeleBot('1045088725:AAF2_sz5hTJo7kTjPn8m06jzGzoDMDmp_mQ');

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет,с помощью меня ты можешь узнать свои баллы в брс: Нужно написать свое ФИО, каждое слово с большой буквы')
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    name_students = back.main(message.text)
    if "Такого" in name_students:
        bot.send_message(message.from_user.id,str(name_students))
    else:
        bot.send_message(message.from_user.id,str(name_students))
bot.polling()

