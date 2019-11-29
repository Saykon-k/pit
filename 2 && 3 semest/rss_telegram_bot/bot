import telebot
import feedparser
import atoma, requests

bot = telebot.TeleBot('% по сооброжения безопасности токен был удален %');

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, я многофункциональный бот (с одной функцией), напиши откуда с какого источника брать новости и ключевое слово,пока что доступны два сервиса лента и тех(так и пишите эти сайты))')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
        mes = message.text.lower()
        mes = mes.split()
        if len(mes) == 2:
            lenta = mes[0]
            slovo = mes[1]
        
            if lenta == 'лента':
                url= "https://lenta.ru/rss/news"
            elif lenta == 'тех':
                url = "https://feeds2.feedburner.com/TheGeeksOf3d"
            else:
                url = ''
            
            if url != '':
                
                feed = feedparser.parse(url)
                case_data = []
        
                for post in feed.entries:
                    if slovo.lower() in post.title.lower().split():
                        case_data.append([post.title, post.link])

                if len(case_data) == 0:
                    bot.send_message(message.from_user.id,"Ничего не было найдено по вашему запросу")
                else:
                    for i in range(len(case_data)):
                        bot.send_message(message.from_user.id,case_data[i][0] + " " + case_data[i][1] )
            else:
                bot.send_message(message.from_user.id,"Не правильно был указан сайт")
        else:
            bot.send_message(message.from_user.id,"Что-то пошло не так попробуйте еще раз!!!!(Я в вас верю(возможно))")

bot.polling()
