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

def add_place(hall_id, place_key, status):
   h = models.Halls.query.filter(models.Halls.id == hall_id).first()
   p = models.Place(hall_id = hall_id, status = status, id_key=place_key)
   db.session.add(p)
   db.session.commit()




@app.route('/addbp', methods=['GET', 'POST'])
def AddBusyPlace():
    s = (request.get_data()).decode('utf-8')
    d = json.loads(s)
    hall_id = d['hall_id']
    place_key = d['place_key']
    status = d['status']
    add_place(hall_id= hall_id, place_key=place_key, status=status)
    h = models.Place.query.filter(models.Place.hall_id == int(d['hall_id'])).all()
    return packjson.pack_busy_places(h)


@app.route('/ch', methods=['GET', 'POST'])
def CreateHall():
    s = (request.get_data()).decode('utf-8')
    d = json.loads(s)
    image = packjson.create_image_from_base64(d['image'])
    h = models.Halls(restourant_id = d['rest_id'], name = d['name'],  count = d['count'], image = image)
    db.session.add(h)
    db.session.commit()
    return 'success'


@app.route('/ghs', methods=['GET', 'POST'])
def GetHalls():
    s = (request.get_data()).decode('utf-8')
    d = json.loads(s)
    id=d['id']
    h = models.Halls.query.filter(models.Halls.restourant_id == id).all()
    if h!=None: return packjson.pack_halls(h)
    return 'None'




@app.route('/gbp', methods=['GET', 'POST'])
def GetBusyPlaces():
    s = (request.get_data()).decode('utf-8')
    d = json.loads(s)
    h = models.Place.query.filter(models.Place.hall_id == int(d['hall_id'])).all()
    return packjson.pack_busy_places(h)



