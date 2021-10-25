# -*- coding: utf-8 -*-

from app import db
from sqlalchemy_serializer import SerializerMixin

class dateTime(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    week_id = db.Column(db.Integer, db.ForeignKey('week.id'))
    date = db.Column(db.String(64), index = True, unique = False)
    timeStart = db.Column(db.String(64), index=True, unique=False)
    timeStop = db.Column(db.String(64), index=True, unique=False)





class Week(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key = True)
    Monday_start = db.Column(db.String(120), index=True, unique=False)
    Monday_stop = db.Column(db.String(120), index=True, unique=False)
    Tuesday_start = db.Column(db.String(120), index = True, unique = False)
    Tuesday_stop = db.Column(db.String(120), index=True, unique=False)
    Wednesday_start = db.Column(db.String(120), index = True, unique = False)
    Wednesday_stop = db.Column(db.String(120), index=True, unique=False)
    Thursday_start = db.Column(db.String(120), index = True, unique = False)
    Thursday_stop = db.Column(db.String(120), index=True, unique=False)
    Friday_start = db.Column(db.String(120), index = True, unique = False)
    Friday_stop = db.Column(db.String(120), index=True, unique=False)
    Saturday_start = db.Column(db.String(120), index = True, unique = False)
    Saturday_stop = db.Column(db.String(120), index=True, unique=False)
    Sunday_start = db.Column(db.String(120), index = True, unique = False)
    Sunday_stop = db.Column(db.String(120), index=True, unique=False)
    datetime = db.relationship("dateTime", backref="datetime_id", lazy="dynamic")
    restourant_id = db.Column(db.Integer, db.ForeignKey('restourant.id'))
    def setData(self, data):
        self.Monday_start = data[0]
        self.Monday_stop = data[1]
        self. Tuesday_start = data[2]
        self.Tuesday_stop = data[3]
        self.Wednesday_start = data[4]
        self.Wednesday_stop = data[5]
        self.Thursday_start = data[6]
        self.Thursday_stop = data[7]
        self.Friday_start = data[8]
        self.Friday_stop = data[9]
        self.Saturday_start =data[10]
        self.Saturday_stop = data[11]
        self.Sunday_start = data[12]
        self.Sunday_stop = data[13]
        return self




class User(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key = True)
    password = db.Column(db.String(120), index = True, unique = False)
    phone = db.Column(db.String(120), index = True, unique = False)
    first_name = db.Column(db.String(120), index = True, unique = False)
    last_name = db.Column(db.String(120), index = True, unique = False)
    email = db.Column(db.String(120), index = True, unique = False)
    dateOfBurn = db.Column(db.String(120), index = True, unique = False)

    #role = db.Column(db.SmallInteger, default = ROLE_USER)



class Restourant(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120), index = True, unique = False)
    icon = db.Column(db.String(64), index = True, unique = False)
    description = db.Column(db.String(1000), index = True, unique = False)
    phone = db.Column(db.String(64), index = True, unique = False)
    address = db.Column(db.String(120), index = True, unique = False)
    coordinates = db.Column(db.String(120), index = True, unique = False)
    www = db.Column(db.String(120), index = True, unique = False)
    time = db.Column(db.String(120), index = True, unique = False)
    all = db.Column(db.String(1200), index=True, unique=False)
    rating = db.Column(db.String(120), index = True, unique = False)
    email = db.Column(db.String(120), index = True, unique = False)
    cost = db.Column(db.Float, index = True, unique = False)
    kitchenType = db.Column(db.String(256), index = True, unique = False)
    restourantType = db.Column(db.String(256), index=True, unique=False)
    gallery=db.relationship('Gallery', backref = 'gallery_id', lazy = 'dynamic')
    password = db.Column(db.String(120), index=True, unique=False)
    token = db.Column(db.String(120), index=True, unique=False)
    menu = db.relationship('Menus', backref = 'menus_id', lazy = 'dynamic')
    halls = db.relationship("Halls", backref="halls_id", lazy = "dynamic")
    week = db.relationship("Week", backref="week_id", lazy = "dynamic")

''

    #role = db.Column(db.SmallInteger, default = ROLE_USER)

class Gallery(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key = True)
    path = db.Column(db.String(64), index = True, unique = False)
    restourant_id = db.Column(db.Integer, db.ForeignKey('restourant.id'))


class Menus(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), index = True, unique = False)
    description = db.Column(db.String(1000), index = True, unique = False)
    composition = db.Column(db.String(1000), index = True, unique = False)
    cost = db.Column(db.Float, index = True, unique =  False)
    image = db.Column(db.String(120), index = True, unique =  False)
    weight = db.Column(db.String(64), index = True, unique = False)
    category = db.Column(db.String(64), index=True, unique=False)
    availability = db.Column(db.Boolean, index = True, unique =  False)
    restourant_id = db.Column(db.Integer, db.ForeignKey('restourant.id')) # ассоциирует поле id таблицы Restourant с полем  restt_id таблицы Menus
    #rest_id = db.Column(db.Integer, index = True, unique = False)

    #role = db.Column(db.SmallInteger, default = ROLE_USER)



class Order(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key = True)
    token = db.Column(db.String(64), index=True, unique=False)
    user_id = db.Column(db.String(64), index = True, unique = False)
    restourant_id = db.Column(db.String(120), index = True, unique = False)
    menus_id = db.Column(db.String(1024), index = True, unique =  False)
    n_table = db.Column(db.String(64), index = True, unique =  False)
    n_peopls = db.Column(db.String(64), index = True, unique =  False)
    is_accepted = db.Column(db.Boolean, index=True, unique=False)
    is_executed = db.Column(db.Boolean, index=True, unique=False)
    datatime = db.Column(db.String(32), index=True, unique=False)



class Halls(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(64), index = True, unique = False)
    count = db.Column(db.Integer, index=True)
    name =  db.Column(db.String(64), index = True, unique = False)
    restourant_id = db.Column(db.Integer, db.ForeignKey('restourant.id'))
    places = db.relationship("Place", backref="place_id", lazy="dynamic")


class Place(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    id_key = db.Column(db.String(512), index=True, unique=False)
    status = db.Column(db.String(512), index = True, unique = False)
    hall_id = db.Column(db.Integer, db.ForeignKey('halls.id'))
