# -*- coding: utf-8 -*-
import random
from app import security
from app import packjson
from app import app
from flask import request
from app import db, models
import random
import json
import base64
from flask import send_from_directory
from flask import render_template, flash, redirect
import os
from app import FCM
#from app import views_admin




# Контроллер удаления блюда
@app.route('/dm', methods=['GET', 'POST'])
def del_menu_admin():
    s = (request.get_data()).decode('utf-8')
    d=json.loads(s)
    menu = models.Menus.query.filter(models.Menus.id == d['id'])
    if menu.image != 'XXXL.jpg': os.remove(packjson.root + menu.image)
    menu = models.Menus.query.filter(models.Menus.id==d['id']).delete()
    db.session.commit()
    return "success"




# Контроллер обновления блюда ресторана
@app.route('/um', methods=['GET', 'POST'])
def update_menu_admin():
    s = (request.get_data()).decode('utf-8')
    d=json.loads(s)
    menu = models.Menus.query.get(int(d['id']))
    menu.name = d['name']
    menu.description = d['description']
    menu.composition = d['composition']
    menu.cost = d['cost']
    availability = d['availability']
    if menu.image != 'XXXL.jpg': os.remove(packjson.root + menu.image)
    menu.image = packjson.create_image_from_base64(d['image'])
    db.session.add(menu)
    db.session.commit()
    return 'sucess'

# Контроллер создания блюда ресторана
@app.route('/cm', methods=['GET', 'POST'])
def create_menu_admin():
    s = (request.get_data()).decode('utf-8')
    d=json.loads(s)

    m = models.Menus(name='Название блюда ', composition='Состав блюда ',
                     description='Краткое, но ёмкое описание блюда', image='XXXL.jpg', cost='320',
                     restourant_id=d['id'])
    db.session.add(m)
    db.session.commit()
    menu = models.Menus.query.filter(models.Menus.restourant_id == d['id'])
    str = packjson.pack_menu(menu)
    return str


# Контроллер получения меню ресторана
@app.route('/gma', methods=['GET', 'POST'])
def get_menu_admin():
    s = (request.get_data()).decode('utf-8')
    d=json.loads(s)
    menu = models.Menus.query.filter(models.Menus.restourant_id==d['id'])
    str = packjson.pack_menu(menu)
    return str
