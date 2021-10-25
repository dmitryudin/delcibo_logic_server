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


# контроллер создания заказа
@app.route('/co', methods=['GET', 'POST'])
def create_order():
    s = (request.get_data()).decode('utf-8')
    d = json.loads(s)

    menus = json.dumps(d['order']) # создаётся json с объектом заказов
    tok = packjson.buildRandomString(30)
    u = models.Order(user_id=d['user_id'], restourant_id=d['restaurant_id'], menus_id=menus, token=tok)
    i = db.session.add(u)
    db.session.commit()
    rest = models.Restourant.query.get(int(d['restaurant_id']))
    FCM.send_message(rest.token, "Новый заказ!!!", "Нажмите чтобы посмотреть")
    order = models.Order.query.filter(models.Order.token == tok).first()
    id = order.id

    return '{"id":'+str(id)+'}'