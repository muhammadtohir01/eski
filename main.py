from telegram.ext import Updater,CommandHandler,CallbackContext,MessageHandler,Filters,CallbackQueryHandler
from telegram import Update,ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton,Bot
import os

# 5890078738:AAG9qDaSHqRjVDuzTNdgAFu73HPqB9sd1Hw
# get token from env
TOKEN = os.environ['TOKEN']



def start(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id

    keyboar = ReplyKeyboardMarkup([
        ['🛍 Videolar','Rasmlar']
    ])
    bot = context.bot
    bot.sendMessage(
    chat_id=chat_id,
    text='Assalom alaykum😘😘❤️😘😘',
    reply_markup=keyboar
    )


def roli(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id

    video1 = InlineKeyboardButton(text='video1',callback_data='video11')
    video2 = InlineKeyboardButton(text='video2',callback_data='video12')
    video3 = InlineKeyboardButton(text='video3',callback_data='video13')
    video4 = InlineKeyboardButton(text='video4',callback_data='video14')
    video5= InlineKeyboardButton(text='video5',callback_data='video15')
    video6= InlineKeyboardButton(text='video6',callback_data='video16')
    video7 = InlineKeyboardButton(text='video7',callback_data='video17')
    video8 = InlineKeyboardButton(text='video8',callback_data='video18')
    video9 = InlineKeyboardButton(text='video9',callback_data='video19')
    video10 = InlineKeyboardButton(text='video10',callback_data='video20')
    video11= InlineKeyboardButton(text='video11',callback_data='video21')
    video12= InlineKeyboardButton(text='video12',callback_data='video22')
    video13= InlineKeyboardButton(text='video13',callback_data='video23')
    video14= InlineKeyboardButton(text='video14',callback_data='video24')
    video15= InlineKeyboardButton(text='video15',callback_data='video25')
    video16= InlineKeyboardButton(text='video16',callback_data='video26')

    # Define keyboard
    keyboar = InlineKeyboardMarkup([
        [video1,video2,video3],
        [video4,video5,video6],
        [video7,video8,video9],
        [video10,video11,video12],
        [video13,video14,video15],
        [video16]
    ])

    bot = context.bot
    bot.sendMessage(chat_id=chat_id,text='❤️Videolar❤️',reply_markup=keyboar)

# Rasmlar
def toli(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id

    rasm1 = InlineKeyboardButton(text='rasm1',callback_data='rasm11')
    rasm2 = InlineKeyboardButton(text='rasm2',callback_data='rasm12')
    rasm3 = InlineKeyboardButton(text='rasm3',callback_data='rasm13')
    rasm4 = InlineKeyboardButton(text='rasm4',callback_data='rasm14')
    rasm5= InlineKeyboardButton(text='rasm5',callback_data='rasm15')
    rasm6= InlineKeyboardButton(text='rasm6',callback_data='rasm16')
    rasm7 = InlineKeyboardButton(text='rasm7',callback_data='rasm17')
    rasm8 = InlineKeyboardButton(text='rasm8',callback_data='rasm18')
    rasm9 = InlineKeyboardButton(text='rasm9',callback_data='rasm19')
    rasm10 = InlineKeyboardButton(text='rasm10',callback_data='rasm20')
    rasm11= InlineKeyboardButton(text='rasm11',callback_data='rasm21')
    rasm12= InlineKeyboardButton(text='rasm12',callback_data='rasm22')
    rasm13= InlineKeyboardButton(text='rasm13',callback_data='rasm23')
    rasm14= InlineKeyboardButton(text='rasm14',callback_data='rasm24')
    rasm15= InlineKeyboardButton(text='rasm15',callback_data='rasm25')
    rasm16= InlineKeyboardButton(text='rasm16',callback_data='rasm26')
    rasm17= InlineKeyboardButton(text='rasm17',callback_data='rasm27')
    rasm18= InlineKeyboardButton(text='rasm18',callback_data='rasm28')
    rasm19= InlineKeyboardButton(text='rasm19',callback_data='rasm29')
    rasm20= InlineKeyboardButton(text='rasm20',callback_data='rasm30')
    # Define keyboard
    keyboar = InlineKeyboardMarkup([
        [rasm1,rasm2,rasm3],
        [rasm4,rasm5,rasm6],
        [rasm7,rasm8,rasm9],
        [rasm10,rasm11,rasm12],
        [rasm13,rasm14,rasm15],
        [rasm16,rasm17,rasm18],
        [rasm19,rasm20]
    ])

    bot = context.bot
    bot.sendMessage(chat_id=chat_id,text='❤️Rasmlar❤️',reply_markup=keyboar)
    
    # Query
def query(update: Update, context: CallbackContext):
    query= update.callback_query
    chat_id = query.message.chat_id
    data = query.data
    bot = context.bot
    if data=='video11':
        video="BAACAgIAAxkBAAPGY_OwIjXbLFuJgSS69O21HN1Vo3MAAh8mAAIqGJlLlS5uurDk9mcuBA"
        bot.sendVideo(chat_id=chat_id,video=video)
    if data=='video12':
        video = "BAACAgIAAxkBAAPHY_OwTW327U9wDqMWNS_ta-SYijYAAiAmAAIqGJlLiLJdtKn9Y1guBA"
        bot.sendVideo(chat_id=chat_id,video=video)
            
    elif data=='video13':
        video = "BAACAgIAAxkBAAPIY_OwZ4SOir1yMG6V1_RzOlQCcjoAAiEmAAIqGJlLJk7nMhZr260uBA"
        bot.sendVideo(chat_id=chat_id,video=video)

    elif data=='video14':
        video = "BAACAgIAAxkBAAPJY_OwhZM75fJ-CjSkwxtbRwGZGTYAAiQmAAIqGJlLXR1m8xvJrPkuBA"
        bot.sendVideo(chat_id=chat_id,video=video)
        
    elif data=='video15':
        video = "BAACAgIAAxkBAAPKY_OwssE7_yMHHaf6Oq_SLJrhe1gAAhsmAAIqGJlLyfbpHQ5HJ-suBA"
        bot.sendVideo(chat_id=chat_id,video=video)

    elif data=='video16':
        video = "BAACAgIAAxkBAAPLY_Ow4Zd-ksrtNNE-MAsp5yAQjNIAAtokAAJ0C6FKL9n6u3Xt8C8uBA"
        bot.sendVideo(chat_id=chat_id,video=video)

    elif data=='video17':
        video = "BAACAgIAAxkBAAPMY_OxIIJ22tuFTBHrwY3CYF3sQHcAAtkkAAJ0C6FKDQGRMDA7GrkuBA"
        bot.sendVideo(chat_id=chat_id,video=video)


    elif data=='video18':
        video="BAACAgIAAxkBAAPNY_OxQI4n3C-bNTRiZXC1BkAFS3AAAuokAAJ0C6FKs74QLXBMCAMuBA"
        bot.sendVideo(chat_id=chat_id,video=video)
        

    elif data=='video19':
        video="BAACAgIAAxkBAAPOY_OyBkxp2lT_K5IxTXEeJ1BVM50AAgUlAAJ0C6FK6Q01dsaYAtcuBA"
        bot.sendVideo(chat_id=chat_id,video=video)

    elif data=='video20':
        video ="BAACAgIAAxkBAAPPY_OyNQqTmHCWbYqHQQ32jAfiJc4AAoYoAALhBqBKVpnB6DvoAk8uBA"
        bot.sendVideo(chat_id=chat_id,video=video)

    elif data=='video21':
        video ="BAACAgIAAxkBAAPQY_OyYXgEjnQxT3qVgIpooRHtb2cAAk8mAAJM1MhKZcTrG-UaeS4uBA"
        bot.sendVideo(chat_id=chat_id,video=video)
        
    elif data=='video22':
        video ="BAACAgIAAxkBAAPRY_OzjeJQojfWr81gCfHirz5etIoAAlIuAAJdpqBLagxl9oZKFusuBA"
        bot.sendVideo(chat_id=chat_id,video=video)

    elif data=='video23':
        video ="BAACAgIAAxkBAAIBG2P0tSVppo7ZAAEfLz_8Hyqet-U_pgACySgAAlGqWEoN3zgctSc1HC4E"
        bot.sendVideo(chat_id=chat_id,video=video)

    elif data=='video24':
        video ="BAACAgIAAxkBAAIBHGP0tXuTfCkcq9ROlrqcgHL71SMTAALIKAACUapYSg2nJhWeK-NbLgQ"
        bot.sendVideo(chat_id=chat_id,video=video)

    elif data=='video25':
        video ="BAACAgIAAxkBAAIBHWP0taTtDt4cdRsEg2eK5cNt1DbJAALHKAACUapYSoSdUeLpF-MzLgQ"
        bot.sendVideo(chat_id=chat_id,video=video)

    elif data=='video26':
        video ="BAACAgIAAxkBAAIBHmP0tsL4zefWbuf6clIkvF6T7aQ3AALGKAACUapYSkkHffhPLV-LLgQ"
        bot.sendVideo(chat_id=chat_id,video=video)


    
    # Rsamlar
    elif data=='rasm11':
        photo ="AgACAgIAAxkBAAPnY_SpKd5x42glwMxwW8fRMWXuEtsAAqrHMRv-a6FL7bWsnwOJDB4BAAMCAANzAAMuBA"
        bot.sendPhoto(chat_id=chat_id,photo=photo)

    elif data=='rasm12':
        photo ="AgACAgIAAxkBAAPzY_SquHRr98J8wTOW39tSCJbZ-PUAAq_HMRv-a6FLksk8F2b3Qv0BAAMCAANzAAMuBA"
        bot.sendPhoto(chat_id=chat_id,photo=photo)

    elif data=='rasm13':
        photo ="AgACAgIAAxkBAAP1Y_SsDQNBiQ3tTIRKEi99rCCQ4DIAAqzHMRv-a6FLfxqbRTTkdpsBAAMCAANzAAMuBA"
        bot.sendPhoto(chat_id=chat_id,photo=photo)

    elif data=='rasm14':
        photo= "AgACAgIAAxkBAAIBCWP0rVUt0TFQSwuxXAGwmRPq4UBkAAKzxzEb_muhS56Hgxi-NSPIAQADAgADcwADLgQ"
        bot.sendPhoto(chat_id=chat_id,photo=photo)

    elif data=='rasm15':
        photo="AgACAgIAAxkBAAIBX2P0vrOrP7_JwePZErADUosWw2GTAAKrxzEb_muhS3MQ5LHv11btAQADAgADcwADLgQ"
        bot.sendPhoto(chat_id=chat_id,photo=photo)

    elif data=='rasm16':
        photo="AgACAgIAAxkBAAIBC2P0ryxZlmRT0ZRX_KXPMJnzmnGeAAKpxzEb_muhS-s_JGTVx-2xAQADAgADcwADLgQ"
        bot.sendPhoto(chat_id=chat_id,photo=photo)

    elif data=='rasm17':
        photo ="AgACAgIAAxkBAAIBDGP0r3Y3pkNp-7ZTmL6bo1cT1cgDAAKoxzEb_muhS5aJbPmAxLBlAQADAgADcwADLgQ"
        bot.sendPhoto(chat_id=chat_id,photo=photo)

    elif data=='rasm18':
        photo="AgACAgIAAxkBAAIBDWP0r82kyari5c6YX-5l65Ws2s33AAKnxzEb_muhS3RHcBbVriHlAQADAgADcwADLgQ"
        bot.sendPhoto(chat_id=chat_id,photo=photo)

    elif data=='rasm19':
        photo="AgACAgIAAxkBAAIBDmP0sBqoTmk1yNa6eUhfM3UELbPOAAKlxzEb_muhS-Aj_HczqZxPAQADAgADcwADLgQ"
        bot.sendPhoto(chat_id=chat_id,photo=photo)

    elif data=='rasm20':
        photo="AgACAgIAAxkBAAIBD2P0sF-kDwqTC4663B9bQfADxGzqAAKkxzEb_muhSyItladZ37m3AQADAgADcwADLgQ"
        bot.sendPhoto(chat_id=chat_id,photo=photo)

    elif data=='rasm21':
        photo="AgACAgIAAxkBAAIBEGP0sKZeOe914VaJboJ0YAT2EtcaAAKjxzEb_muhS15l_g2ArAJUAQADAgADcwADLgQ"
        bot.sendPhoto(chat_id=chat_id,photo=photo)

    elif data=='rasm22':
        photo ="AgACAgIAAxkBAAIBEWP0sOzZKCoYRiqvf3QP5SYIiiWCAAKixzEb_muhS72KSXSZKe1gAQADAgADcwADLgQ"
        bot.sendPhoto(chat_id=chat_id,photo=photo)

    elif data=='rasm23':
        photo="AgACAgIAAxkBAAIBEmP0sUi-TLn01oPKhZhpj0OzX5isAAKfxzEb_muhS9Rkt1RTRTJHAQADAgADcwADLgQ"
        bot.sendPhoto(chat_id=chat_id,photo=photo)

    elif data=='rasm24':
        photo="AgACAgIAAxkBAAIBE2P0sjq9HFFNUM2DKESFiNcBX4x-AAKmwzEbUapYSorezH39f2pVAQADAgADcwADLgQ"
        bot.sendPhoto(chat_id=chat_id,photo=photo)

    elif data=='rasm25':
        photo ="AgACAgIAAxkBAAIBFGP0sn9eciQ5SNwyfXzxvoqc1P5MAAKfwzEbUapYSrL7o1HUlAOKAQADAgADcwADLgQ"
        bot.sendPhoto(chat_id=chat_id,photo=photo)

    elif data=='rasm26':
        photo="AgACAgIAAxkBAAIBFWP0svYHl1dZ7ZkgtCkN6vohRhidAAKkwzEbUapYSpN8tvMYilK4AQADAgADcwADLgQ"
        bot.sendPhoto(chat_id=chat_id,photo=photo)

    elif data=='rasm27':
        photo= "AgACAgIAAxkBAAIBFmP0s0aYi_ln8DSyAAFn3wY_Pf9EaQACqMMxG1GqWEpjuMgatTfq_AEAAwIAA3MAAy4E"
        bot.sendPhoto(chat_id=chat_id,photo=photo)

    elif data=='rasm28':
        photo="AgACAgIAAxkBAAIBF2P0s7tj_XL0Rx_hDnvlZdWoiG2LAAKjwzEbUapYSq10RRRWKS6XAQADAgADcwADLgQ"
        bot.sendPhoto(chat_id=chat_id,photo=photo)

    elif data=='rasm29':
        photo="AgACAgIAAxkBAAIBGWP0tFw40Ui5MMK1BUP4wVzfFRSkAAKdwzEbUapYSsQ6fwjLSe6mAQADAgADcwADLgQ"
        bot.sendPhoto(chat_id=chat_id,photo=photo)

    elif data=='rasm30':
        photo="AgACAgIAAxkBAAIBGmP0tKQPw147t2frB5AHuCnW7alGAAKewzEbUapYSkjY2NeZKZ_EAQADAgADcwADLgQ"
        bot.sendPhoto(chat_id=chat_id,photo=photo)
  
    query.answer('Hi')


def ali():
     
    updater = Updater(token=TOKEN)
    updater.dispatcher.add_handler(CommandHandler('start',start))
    # Add handler for photo message
    updater.dispatcher.add_handler(MessageHandler(Filters.text('🛍 Videolar'),roli))
    updater.dispatcher.add_handler(MessageHandler(Filters.text('Rasmlar'),toli))
    updater.dispatcher.add_handler(CallbackQueryHandler(query))

    updater.start_polling()
    updater.idle()