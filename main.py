import telebot
from telebot import types

bot = telebot.TeleBot('5208782181:AAGTZm_HtB0QUmANjAzYxTg5xHHMpdJLK44')

@bot.message_handler(commands=['start'])
def start(message):
    mess = (f'Салам, <b>{message.from_user.first_name} {message.from_user.first_name}</b>!' +
            '\nТы залетел на бота сам знаешь какого хорошего человека!' +
            '\n<i>Здесь ты можешь больше узнать о Никитке, получить ссылку на его сайт, найти контакты' +
            ' для связи с ним и еще много всего другого...</i>')

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    contacts = types.KeyboardButton('My Contacts')
    music = types.KeyboardButton('True Music')
    video = types.KeyboardButton('True Video')
    markup.add(contacts, music, video)
    bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)

    photo = open('resources/start_photo.jpg', 'rb')
    markupl = types.InlineKeyboardMarkup()
    markupl.add(types.InlineKeyboardButton("код этого бота на GitHub", url='https://github.com/qowepo/-TelegramBot'))
    bot.send_photo(message.chat.id, photo, reply_markup=markupl)


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Бог поможет!')


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == "True Music":
        photo = open('resources/music_photo.jpg', 'rb')
        audio1 = open('resources/Колхозники.mp3', 'rb')
        audio = open('resources/до зимы.mp3', 'rb')
        audio2 = open('resources/Outro.mp3', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_audio(message.chat.id, audio1)
        bot.send_audio(message.chat.id, audio)
        bot.send_audio(message.chat.id, audio2)

    elif message.text == "True Video":
        video = open('resources/send_video.mp4', 'rb')
        bot.send_video(message.chat.id, video)

    elif message.text == "My Contacts":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        Vk = types.KeyboardButton('Vk')
        Inst = types.KeyboardButton('Instagram')
        Syte = types.KeyboardButton('My Site')
        Git = types.KeyboardButton('My GitHub')
        Head = types.KeyboardButton('Back to main page')
        markup.add(Vk, Inst, Syte, Git, Head)
        photo = open('resources/contacts.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, '\nE-mail: nikulinn3349@gmail.com', reply_markup=markup)

    elif message.text == "My Site":
        photo = open('resources/syte.jpg', 'rb')
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Ссылочка на сайтик", url='https://qowepo.github.io/'))
        bot.send_photo(message.chat.id, photo, reply_markup=markup)

    elif message.text == "Instagram":
        photo = open('resources/instagram.jpg', 'rb')
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Ссылочка на инстаграмчик", url='https://www.instagram.com/qowepo'))
        bot.send_photo(message.chat.id, photo, reply_markup=markup)

    elif message.text == "Vk":
        photo = open('resources/vk.jpg', 'rb')
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Ссылочка на vk", url='https://vk.com/qowepo'))
        bot.send_photo(message.chat.id, photo, reply_markup=markup)

    elif message.text == "My GitHub":
        photo = open('resources/github.jpg', 'rb')
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Ссылочка на github", url='https://github.com/qowepo'))
        bot.send_photo(message.chat.id, photo, reply_markup=markup)

    elif message.text == "Back to main page":
        mess = (f'Салам, <b>{message.from_user.first_name} {message.from_user.first_name}</b>!' +
                '\nТы залетел на бота сам знаешь какого хорошего человека!' +
                '\n<i>Здесь ты можешь больше узнать о Никитке, получить ссылку на его сайт, найти контакты' +
                ' для связи с ним и еще много всего другого...</i>')

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        contacts = types.KeyboardButton('My Contacts')
        music = types.KeyboardButton('True Music')
        video = types.KeyboardButton('True Video')
        markup.add(contacts, music, video)
        bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)

        photo = open('resources/start_photo.jpg', 'rb')
        markupl = types.InlineKeyboardMarkup()
        markupl.add(types.InlineKeyboardButton("код этого бота на GitHub", url='https://vk.com/qowepo'))
        bot.send_photo(message.chat.id, photo, reply_markup=markupl)

    else:
        bot.send_message(message.chat.id,
                         'Ты чего мне пишешь дурачок, я всего лишь Бот и понимаю только заданные команды!' +
                         '\n<i>Лучше кинь мне мем, смешной видосик или стикер...</i>' +
                         '\n\nА текст <a href="https://vk.com/qowepo">ЕМУ</a>, на вот, пиши!\n\n', parse_mode='html')


@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    photo = open('resources/send_photo.jpg', 'rb')
    bot.send_photo(message.chat.id, photo, 'а ты хорош')


@bot.message_handler(content_types=['video'])
def get_user_video(message):
    video = open('resources/send_video.mp4', 'rb')
    bot.send_video(message.chat.id, video)


@bot.message_handler(content_types=['sticker'])
def get_user_stiker(message):
    sticker = open('resources/send_sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, sticker)


bot.polling(none_stop=True)