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




@app.route('/cu', methods=['GET', 'POST'])
def create_user():
    s = (request.get_data()).decode('utf-8')
    d=json.loads(s)
    if (not security.isEnterPhoneValid(d['phone'])): return "{'status':'invalid phone'}"

    if (not security.isEnterEmailValid(d['email'])):  return "{'status':'invalid email'}"
    if (security.isUserExists(d['phone'], d['email'])): return "{'status':'user exist'}"
    else:
        u = models.User(first_name=d['first_name'], password=d['password'], phone=d['phone'], last_name=d['last_name'], email=d['email'], dateOfBurn = d['dateofburn,.'])
        db.session.add(u)
        db.session.commit()
        return "{'status':'success'}"