import telebot
    
    # Замени 'TOKEN' на токен твоего бота
    # Этот токен ты получаешь от BotFather, чтобы бот мог работать
sigmabot = telebot.TeleBot("7420968680:AAEypibz6LynVhgtUpKHv26H49Nl1dOV0dM")
    
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")
    
    @bot.message_handler(commands=['hello'])
    def send_hello(message):
        bot.reply_to(message, "Привет! Как дела?")
    
    @bot.message_handler(commands=['bye'])
    def send_bye(message):
        bot.reply_to(message, "Пока! Удачи!")
    
    
    @bot.message_handler(func=lambda message: True)
    def echo_all(message):
        bot.reply_to(message, message.text)
    
    bot.polling()