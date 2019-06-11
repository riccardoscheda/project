#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 17:48:50 2018

@author: riccardo
"""
import telebot  #Telegram Bot API

bot = telebot.TeleBot('741605487:AAGqpMtFxMEvHXnwxsIc4UvLd4q_0JRJGy0')

@bot.message_handler(commands=['start','go'])
def send_welcome(message):
        name = message.chat.id

        bot.send_message(name, "Welcome" + str(name))

bot.polling()
#
# bot.message_loop(rispondi)
# while 1:
#  time.sleep(10)
