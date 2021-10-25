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
from flask import send_from_directory
import os
from app import FCM

@app.route('/templates/<path:path1>', methods=['GET', 'POST'])
def sendFile(path1):
    return send_from_directory('/root/delcibo/app/templates/', path1)

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index1():

    return render_template('cr.html')