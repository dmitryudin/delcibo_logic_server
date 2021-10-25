# -*- coding: utf-8 -*-
from app import app


context = ('server.crt', 'server.key')
app.run(debug = True, host = '94.228.121.2', port = 50)# ssl_context=context)
