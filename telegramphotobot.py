import telebot

bot = telebot.TeleBot('')

@bot.message_handler()
def get_user_text(message):

    if message.text == "Hello":#text
        bot.send_message(message.chat.id, "How are you?")

    elif message.text == "id": #id
        bot.send_message(message.chat.id, f"id: {message.from_user.id}")

    elif message.text == "eth": # photo
        photo = open('images/eth.png', 'rb') 
        bot.send_photo(message.chat.id, photo)

    elif message.text == "nora":
        photo = open('images/3.jpeg', 'rb') 
        bot.send_photo(message.chat.id, photo)

    elif message.text == "kolkata":
        photo = open('images/4.jpeg', 'rb') 
        bot.send_photo(message.chat.id, photo)

    elif message.text == "adult":
        photo = open('images/6.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)

    elif message.text == "guma":
        photo = open('images/2.jpg', 'rb') 
        bot.send_photo(message.chat.id, photo)

    elif message.text == "lena":
        photo = open('images/1.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)

    elif message.text == "tatto":
        photo = open('images/5.jpeg', 'rb') 
        bot.send_photo(message.chat.id, photo)

    else:
        bot.send_message(message.chat.id, 'Thank You')

bot.polling(none_stop=True)
