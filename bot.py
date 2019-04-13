#input your telegram token in config.py

import config
import telebot
import pyowm
from telebot import types
import time
import schedule
bot = telebot.TeleBot(config.token)
owm = pyowm.OWM('your token',language='ru')#input your token and language





@bot.message_handler(commands=['start']) #for /start
def handle_start_help(message):
    pass
    bot.send_message(message.chat.id,"Hi,I`m weather telegram bot choose your city") 
    


    markup = types.ReplyKeyboardMarkup()
    
    markup.row('Kramatorsk', 'Donetsk','Vinnytsia','Dnipropetrovsk') #cityes
    markup.row('Kharkiv', 'Lviv', 'Kiev','Zhytomyr')
    markup.row('Zaporizhzhia','Ivano-Frankivsk','Kirovohrad')
    markup.row('Luhansk','Lutsk','Mykolaiv','Odesa')
    markup.row('Poltava','Rivne','Sevastopol','Simferopol')
    markup.row('Sumy','Ternopil','Uzhhorod','Kherson')
    markup.row('Khmelnytskyi','Cherkasy','Chernivtsi','Chernihiv')
    bot.send_message(message.chat.id, "Выберите ваш город", reply_markup=markup)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):   
    if message.text in('Kramatorsk', 'Donetsk','Vinnytsia','Dnipropetrovsk','Kharkiv', 'Lviv', 'Kiev','Zhytomyr','Zaporizhzhia','Ivano-Frankivsk','Kirovohrad','Luhansk','Lutsk','Mykolaiv','Odesa','Poltava','Rivne','Sevastopol','Simferopol','Sumy','Ternopil','Uzhhorod','Kherson','Khmelnytskyi','Cherkasy','Chernivtsi','Chernihiv') : #if invalid city 
        print("all good")
        owm = pyowm.OWM('09b50a8a13c68a6a9fd07f5b256f1d44',language='ru')
        observation = owm.weather_at_place(message.text)
        
        print("ТЕЛЕГРАМ БОТ ЗАПУЩЕН")   
        print(message.text)
        w = observation.get_weather()
        win = w.get_wind() ['speed']
        time = w.get_reference_time(timeformat='iso') 
        hum = w.get_humidity()             
        tempr = w.get_temperature('celsius')['temp']
        cloud = w.get_detailed_status()
        bot.send_message(message.chat.id,"Temperature celsius ")
        bot.send_message(message.chat.id,tempr)
        bot.send_message(message.chat.id,time)
        bot.send_message(message.chat.id,"Wind speed m/s")
        bot.send_message(message.chat.id,win) 
        bot.send_message(message.chat.id,"Humifity in %")
        bot.send_message(message.chat.id,hum)
        bot.send_message(message.chat.id,cloud)

       
        

    else:
        print(message.text)
        bot.send_message(message.chat.id,"Sorry,I don`t understand you please input correct city")


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):   
    
    bot.send_message(message.chat.id, "Choose your city", reply_markup=markup)
if __name__ == '__main__':
     bot.polling(none_stop=True)

if message.text == "exit":
    exit()