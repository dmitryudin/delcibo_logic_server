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



@app.route('/grl', methods=['GET', 'POST'])
@app.route('/getrestorauntlist', methods=['GET', 'POST'])
def grl():
    Restourant1 = models.Restourant.query.all()
    print(request.get_data())
    return packjson.pack_restorant_list(Restourant1)







@app.route('/gallery/<path:path1>', methods=['GET', 'POST'])
def sendGallery(path1):
    return send_from_directory('/root/delcibo/app/static/gallery', path1)

# контроллер получения объекта ресторана полльзователем
@app.route('/gr', methods=['GET', 'POST'])
def get_restaurant():
    s = (request.get_data()).decode('utf-8')
    d=json.loads(s)
    rest = models.Restourant.query.get(int(d['id']))
    return packjson.pack_restorant(rest)






@app.route('/err', methods=['GET', 'POST'])
def users_error():
    s = (request.get_data()).decode('utf-8')
    d = json.loads(s)
    print (s)
    return 'so good'




                                                                                                                  # Контроллер получения объекта ресторана администратором




















def complete_db():
    for i in range(30):
        u = models.User(first_name='user_name '+ str(i), password='password '+ str(i), phone='89507650862', last_name='user_last_name '+ str(i), email='mail'+ str(i)+'@mail.ru', age=str(i))
        db.session.add(u)

    for i in range(30):

        r = models.Restourant(name='rest_name '+ str(i), icon='XXXL.jpg', description='description '+ str(i), phone='89507650862', address='address '+ str(i), email='restmail'+ str(i)+'@mail.ru',cost='120')
        db.session.add(r)
        for j in range(5):
            m = models.Menus(name='menu_name '+ str(j), composition='composition '+ str(j), description='description '+ str(j), image='XXXL.jpg', cost='120', restourant_id=i)
            db.session.add(m)

        g = models.Gallery(path='XXXL.jpg', restourant_id=i)
        db.session.add(g)
        '''
        p = models.Places(image='XXXL.jpg', bisy_places='"Places":[{"No":1, "status":"busy"}, {"No":2, "status":"20.08.2020 15:00"}]',
                         restourant_id=i)
        db.session.add(p)
        '''
        db.session.commit()


   

#complete_db()

#@app.route('/cr/', methods=['GET', 'POST'])
#def create_restaurant():
#	form = restorant_mnt.CreateForm()
#	return render_template('cr.html',title = 'Sign In',form = form)
