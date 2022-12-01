import telebot
#Bot's API token
API_TOKEN = 'TOKEN'

bot = telebot.TeleBot(API_TOKEN)

# Commands
# 1st example
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, """\
I'm working!\
""")
# 2nd example
@bot.message_handler(commands=['commandname'])
def send_welcome(message):
    bot.reply_to(message, """\
...\
""")

# Replies
@bot.message_handler(func=lambda message: True)
def echo_message(message):   
    if message.text=='Hi':
        bot.reply_to(message, 'Hi!')
    elif message.text=='How are you?':
        bot.reply_to(message, 'Fine. Thank you!')
        
bot.polling()
