# -*- coding: utf-8 -*-
import random
from app import security
from app import packjson
from app import app
from flask import request, jsonify
from app import db, models, views_admin, views
import random
import json
import base64
from flask import send_from_directory
from flask import render_template, flash, redirect
import os
from app import FCM
#from app import views_admin


@app.route('/ar', methods=['GET', 'POST'])
def auth_restaurant():
    s = (request.get_data()).decode('utf-8')
    d = json.loads(s)
    try:
        rest = models.Restourant.query.get(int(d['id']))
        if rest!= None: return str(rest.id)
        else: return "no!"
        return str(rest.id)
    except: return "no!"


@app.route('/create_image', methods=['GET', 'POST'])
def create_image():
    s = (request.get_data()).decode('utf-8')
    d=json.loads(s)
    rest = models.Restourant.query.get(int(d['id']))
    base64 = d['base64']
    fileName = packjson.create_image_from_base64(base64)
    if d['category'] == 'gallery':
        g = models.Gallery(path=fileName, restourant_id=rest.id)
        db.session.add(g)
    db.session.commit()

    return 'ok'


@app.route('/delete_image', methods=['GET', 'POST'])
def delete_image():
    s = (request.get_data()).decode('utf-8')
    d=json.loads(s)
    url = d['url']
    path = url.split('/')[-1]
    rest = models.Restourant.query.get(int(d['id']))
    if d['category']=='gallery':
        for gal in rest.gallery:
            if(gal.path==path):
                db.session.delete(gal)
                db.session.commit()
                os.remove(packjson.root+path)
                return '{"status":"ok"}'
    if d['category']=='icon':
        rest.icon = 'None'
        db.session.delete(gal)
        db.session.commit()
        os.remove(packjson.root+path)
        return '{"status":"ok"}'
    return '{"status":"lost"}'

@app.route('/update_image', methods=['GET', 'POST'])
def update_image():
    s = (request.get_data()).decode('utf-8')
    d=json.loads(s)
    rest = models.Restourant.query.get(int(d['id']))
    url=d['url']
    base64 = d['base64']
    requestr = '{"url":"'+packjson.path + security.find_picture(rest, url, base64)+'"}'
    print (requestr)
    return requestr

@app.route('/ur', methods=['GET', 'POST'])
def update_restaurant():
    s = (request.get_data()).decode('utf-8')
    d=json.loads(s)
    rest = models.Restourant.query.get(int(d['id']))
    rest.name = d['name'];
    rest.description = d['description']
    rest.phone = d['phone']
    rest.address = d['address']
    rest.email = d['email']
    rest.cost = d['cost']
    rest.kitchenType = d['kitchenType']
    rest.restourantType = d['restourantType']
    rest.password = d['password']
    db.session.commit()
    rest = models.Restourant.query.get(int(d['id']))
    print(packjson.pack_restorant_for_admin(rest))
    return packjson.pack_restorant_for_admin(rest)








# TODO здесь надо сделать верификайию на существуещего пользователчя и защиту от инъекций
# Это контроллер регистрации нового ресторана
@app.route('/cr', methods=['GET', 'POST'])
def create_restaraunt():
    s = (request.get_data()).decode('utf-8')
    d=json.loads(s)
    if (not security.isEnterPhoneValid(d['phone'])): return "{'status':'invalid phone'}"

    if (not  security.isEnterEmailValid(d['email'])):  return "{'status':'invalid email'}"
    if (security.isRestorauntExists(d['phone'], d['email'])): return "{'status':'restoraunt exist'}"
    else:
        r = models.Restourant(name='Название заведения', icon='XXXL.jpg', description='Краткий обзор (описание) заведения (логотип, особенности интерьера, вид кухни, проводимые мероприятия, наличие игровой площадки (зоны) для детей, музыка',
                              phone=d['phone'], address='Воронеж, 9 Января, 233/17', email=d['email'],
                              cost=0, password = d['password'], coordinates = '', time = 'пн-вс с 8:00 до 00:00', www = 'http://rest.ru', all = 'Пароль от WIFI уточняйте у администратора', rating = '5.0')
        db.session.add(r)
        db.session.commit()
        rest = models.Restourant.query.filter(models.Restourant.phone == d['phone']).first()
        m = models.Menus(name='Название блюда ', composition='Состав блюда ',
                         description='Краткое, но ёмкое описание блюда', image='XXXL.jpg', cost='320', restourant_id=rest.id)
        db.session.add(m)


        g = models.Gallery(path='XXXL.jpg', restourant_id=rest.id)
        db.session.add(g)
        w = models.Week(Monday_start='00:00', Monday_stop='00:00', Tuesday_start='00:00', Tuesday_stop='00:00',  Wednesday_start='00:00', Wednesday_stop='00:00', Thursday_start='00:00',
                        Thursday_stop='00:00', Friday_start='00:00', Friday_stop='00:00', Saturday_start='00:00', Saturday_stop='00:00', Sunday_start='00:00', Sunday_stop='00:00', restourant_id=rest.id)
        db.session.add(w)
        week = models.Week.query.filter(models.Week.restourant_id == rest.id).first()
        dt = models.dateTime(week_id=week.id, date='01.01.2020', timeStart = '00:00', timeStop = '00:00')
        db.session.add(dt)
        db.session.commit()
        return str(rest.id)


# Контроллер обновления токена ресторана
@app.route('/mrt', methods=['GET', 'POST'])
def make_admin_token():
    s = (request.get_data()).decode('utf-8')
    d=json.loads(s)
    rest = models.Restourant.query.get(int(d['id']))
    rest.token=d['token']
    db.session.add(rest)
    db.session.commit()
    return 'sucess'

@app.route('/gra', methods=['GET', 'POST'])
def get_restaurant_admin():
    s = (request.get_data()).decode('utf-8')
    d=json.loads(s)
    rest = models.Restourant.query.get(int(d['id']))

    return packjson.pack_restorant_for_admin(rest)



@app.route('/gw', methods=['GET', 'POST'])
def get_week():
    s = (request.get_data()).decode('utf-8')
    d=json.loads(s)
    week = models.Week.query.filter(models.Week.restourant_id == d['id']).first()
    return packjson.pack_week(week)

@app.route('/uw', methods=['GET', 'POST'])
def update_week():
    s = (request.get_data()).decode('utf-8')
    d=json.loads(s)
    week = models.Week.query.filter(models.Week.restourant_id == d['id']).first()
    #week = models.Week(Sunday=d['Sunday'], Monday=d['Monday'], Tuesday = d['Tuesday'], Wednesday=d['Wednesday'], Thursday=d['Thursday'], Friday=d['Friday'], Saturday = d['Saturday'], restourant_id=d['id'])
    week = week.setData(d['data'])
    db.session.add(week)
    db.session.commit()
    return packjson.pack_week(week)

@app.route('/adt', methods=['GET', 'POST'])
def add_data_time():
    s = (request.get_data()).decode('utf-8')
    d=json.loads(s)
    m = models.Week(Sunday=d['Sunday'], Monday=d['Monday'], Tuesday = d['Tuesday'], Wednesday=d['Wednesday'], Thursday=d['Thursday'], Friday=d['Friday'], Saturday = d['Saturday'], restourant_id=d['id'])
    db.session.add(m)
    db.session.commit()
    return 'sucess'


@app.route('/ddt', methods=['GET', 'POST'])
def delete_data_time():
    s = (request.get_data()).decode('utf-8')
    d=json.loads(s)
    m = models.Week(Sunday=d['Sunday'], Monday=d['Monday'], Tuesday = d['Tuesday'], Wednesday=d['Wednesday'], Thursday=d['Thursday'], Friday=d['Friday'], Saturday = d['Saturday'], restourant_id=d['id'])
    db.session.add(m)
    db.session.commit()
    return 'sucess'
