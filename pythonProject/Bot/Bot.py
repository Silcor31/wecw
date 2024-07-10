import telebot


Bot = telebot.TeleBot('7394893455:AAEgfyovapaDdtRT0LZGaMM9kCK-uexlRpo')

@Bot.message_handler(commands=['start'])
def main(massage):
    #Bot.send_message(massage.chat.id,'Тебе тут делать нечего')
    Bot.send_message(massage.chat.id, 'Бесплатный бот для отметки всех участинков беседы')

@Bot.message_handler(commands=['info'])
def info(info):
    Bot.send_message(info.chat.id,'Для добавления участников необходимо прописать команду <b>/user_name</b>', parse_mode='html')

@Bot.message_handler(commands=['user_name'])
def user_names(name):
    Bot.send_message(name.chat.id, 'Введите ники пользователей без символа <b>@</b>', parse_mode='html')
    names = []
    names.append('@'+str())


@Bot.message_handler()
def all(users):
    if users.text.lower() == '@all':
        Bot.send_message(users.chat.id,'@silcor01, @Yooo_sooo, @hypnotize_mezmerize, @whoisnastyakhen, @Ilya7772023, @siemoishido, @daewooomatizzz, @yas1mple, @IbrishE' )

Bot.polling(none_stop=True)