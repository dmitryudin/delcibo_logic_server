# -*- coding: utf-8 -*-
import os

from app import packjson
from app import db, models
import base64

def find_picture(Restourant, url, Base64):
	filename = url.split('/')[-1]
	try: os.remove(packjson.root + filename)
	except: pass
	print(packjson.root + filename)
	with open(packjson.root + filename, 'wb') as f:
		f.write(base64.b64decode(Base64))
	return filename





def isEnterPhoneValid(phone):
	if len(phone)==11 and (phone.isdigit()): return True
	return False

def isEnterEmailValid(email):
	if (email.find('@')!=-1) and (email.find('.')!=-1): return True
	return False

def isUserAuth1(id):
	data= models.User.query.get(id) # Поиск пользователя по id
	if data==None: return False # Пользователь не найден
	return True # Пользователь найден



def isUserExists(phonee, emaile):
	phonet= models.User.query.filter_by(phone=phonee).first() # Проверка существования пользователя с данным телефоном
	emailt= models.User.query.filter_by(email=emaile).first() # Проверка существования пользователя с данным email
	if phonet==None or emailt==None: return False # Пользователя не существует
	return True # Пользователь существует

# Метод проверки существования ресторана в базе данных
def isRestorauntExists(phonee, emaile):
	try:
		phonet= models.Restourant.query.filter_by(phone=phonee).first() # Проверка существования пользователя с данным телефоном
		emailt= models.Restourant.query.filter_by(email=emaile).first() # Проверка существования пользователя с данным email
		if (phonet!=None and emailt!=None): return True  # Пользователь существует
		else: return False

	except: return False # Пользователя не существует
