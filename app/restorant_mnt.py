# -*- coding: utf-8 -*-


from app import app
from flask import request
from app import db, models
import random
import json
import base64
from flask import send_from_directory
from flask_wtf import Form
from wtforms import TextField, BooleanField
from wtforms.validators import Required

class CreateForm(Form):
    name = TextField('name')
    description = TextField('description')
    phone = TextField('phone')
    address = TextField('address')
    email = TextField('email')
    cost = TextField('cost')
    




'''
 id = db.Colun(db.Integer, primary_key = True)
    name = db.Column(db.String(64), index = True, unique = False)
    description = db.Column(db.String(120), index = True, unique = False)
    phone = db.Column(db.String(120), index = True, unique = True)
    address = db.Column(db.String(120), index = True, unique = False)
    rating = db.Column(db.String(120), index = True, unique = False)
    email = db.Column(db.String(120), index = True, unique = True)
    cost = db.Column(db.Float, index = True, unique = False)
    gallery =db.relationship('Gallery', backref = 'rest_id', lazy = 'dynamic') 
    menu = db.relationship('Menus', backref = 'rest_id', lazy = 'dynamic') 
    '''