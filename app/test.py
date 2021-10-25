# -*- coding: utf-8 -*-
'''
'newUser': [
{
'first_name':'Василий',
'last_name':'Тёркин',
'age': '19',
'email':'example@mail.ru',
'phone':'89191861001',
'password':'123456789'
}]
'''
import json
{"first_name":"Иван","last_name":"p","age": "19","email":"example@mail.ru","phone":"89191861001","password":"123456789"}
string = "{'first_name':'Василий','last_name':'Тёркин','age': '19','email':'example@mail.ru','phone':'89191861001','password':'123456789'}"
s = json.dumps(string)
print(s)

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
db = SQLAlchemy(app)
app.run(debug = True, host = '192.168.43.127', port = 20)
