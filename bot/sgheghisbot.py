#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 17:48:50 2018

@author: riccardo
"""

import telepot
import telebot
import random
import time
import datetime
import string
import json
import requests as req

from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton,ReplyKeyboardRemove,InlineKeyboardButton,InlineKeyboardMarkup


from plumbum import cli, colors
import os
from plumbum import local



orariourl = 'https://corsi.unibo.it/magistrale/Physics/orario-lezioni/@@orario_reale_json?anno=1&amp;curricula=B25-000'
sceglidata = False
understood = False
today = datetime.date.today()
subjects = ["SOFTWARE AND COMPUTING FOR APPLIED PHYSICS","MODELS AND NUMERICAL METHODS IN PHYSICS","X-RAY AND SYNCHROTRON  RADIATION PHYSICS","PATTERN RECOGNITION",
            "COMPLEX NETWORKS","LABORATORIO DI DIDATTICA DELLA FISICA","DIDATTICA DELLA FISICA","PHYSICS IN NEUROSCIENCE AND MEDICINE","PHYSICS OF MEDICAL IMAGING"]


def geturl(url):
  response = req.get(url)
  content = response.content.decode("utf8")
  return content
def getjson(url):
  content = geturl(url)
  js = json.loads(content)
  return js

def getjsonfromorario(orario):
  content = geturl(orario)
  Or = json.loads(content)
  return Or
def orario(chat_id,date):
    day_schedule = []
    room_schedule = []
    h = []
    c = []
    d = []
    orario = getjsonfromorario(orariourl)
    for x in range(len(orario["events"])):
      if orario["events"][x]["date_str"] == date:
        if orario["events"][x]["title"] in subjects:
          day_schedule.append(orario["events"][x]["title"] + " ")
          room_schedule.append(orario["events"][x]["aule"][0]["des_ubicazione"] + " " + orario["events"][x]["aule"][0]["des_risorsa"])
          h.append(orario["events"][x]["time"])

    day_schedule.append(date)
    if len(day_schedule) == 1:
      text = "Il giorno " + date + " sei libero!!!"
      bot.sendMessage(chat_id, text)
    else :
      a = []
      b = []
      num = []
      for x in range(len(day_schedule)-1):
        #day_schedule.sort()
        a.append(day_schedule[x])
        b.append(room_schedule[x])
        c.append(h[x])
        d.append(c[x])
        c[x] = h[x].replace('-',"")
        d[x] = c[x].replace(":00",'')
        d[x] = ''.join(d[x].split())
        num.append(int(d[x]))
        a[x].replace('["',"\t" )
        b[x].replace('["',"\t" )
        if x < len(day_schedule)-1:
          bot.sendMessage(chat_id, a[x] + h[x] + "\nLuogo :\n" + b[x])

def rispondi(msg):
  global understood
  global sceglidata
  global riprova
  chat_id = msg['chat']['id']
  message_id = msg['message_id']
  comando = msg['text'].lower()
  parola = str.split(comando)
  print(parola)
  if "ciao" in comando:
      name = telebot.message.from_user.first_name
      bot.sendMessage(chat_id,"Ciao " + str(chat_id) + " :)")
      understood = True
  if '/start' in comando :
    bot.sendMessage(chat_id,"Ciao! stai usando il bot di Riccardo :)))))) \n Comandi disbonibili: \n /ciao \n /orari")
    understood = True
  if 'orari' in comando :
    today = datetime.date.today()
    text ='Scegli una data'
    bot.sendMessage(chat_id,text,reply_markup=ReplyKeyboardMarkup(keyboard=[[InlineKeyboardButton(text="Oggi\n"+str(today.day)+"/" + str(today.month)), InlineKeyboardButton(text="Domani\n"+ str(today.day+1) + "/" + str(today.month))],[InlineKeyboardButton(text='Scegli data'),InlineKeyboardButton(text='Annulla')]]))
    understood = True
    ReplyKeyboardRemove()
###############
  if 'oggi' in comando:
    today = datetime.date.today()
    tod = str(today.day) + "/" + str(today.month) + "/" + str(today.year)
    bot.sendMessage(chat_id,"Oggi hai:")
    orario(chat_id,tod)
    understood = True
  if 'domani' in comando:
    today = datetime.date.today()
    tom = str(today.day + 1) + "/" + str(today.month) + "/" + str(today.year)
    bot.sendMessage(chat_id,"Domani hai:")
    orario(chat_id,tom)
    understood = True
  if 'data' in comando:
    bot.sendMessage(chat_id,"Scrivi una data in questo formato: DD/MM")
    sceglidata = True
    understood = True
##############
##############
  if ('/' in comando) and (sceglidata == True) :
      tom = str(comando)
      bot.sendMessage(chat_id,"Il giorno " + comando + " hai:")
      orario(chat_id,tom)
      sceglidata = False
      understood = True
##############
##############
  if 'annulla' in comando:
    bot.sendMessage(chat_id,"Comando annullato")
    understood = True
##############
  if "aggiungi" in comando:
      notes = local["notes"]
      notes("add",comando[8:])
      understood = True
  if "lista" in comando:
      notes = local["notes"]
      notes("show")
      understood = True
  if "fatto" in comando:
      notes = local["notes"]
      notes("done",comando[6:])
      understood = True

  if (understood == False) :
    bot.sendMessage(chat_id,"Non ho capito quello che hai scritto, i comandi disponibili sono: \n /start \n ciao \n foto \n orari ")


bot = telepot.Bot('788410342:AAHRDoQsQIHFnn6hgoPRjocohij9JqnR2qY')
bot.message_loop(rispondi)
while 1:
 time.sleep(10)
