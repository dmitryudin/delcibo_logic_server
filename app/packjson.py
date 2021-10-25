import json
import base64
import random
import string

path = 'http://delcibo.ddns.net:80/gallery/'
root = '/root/delcibo/app/static/gallery/'

def get_path(filename):
	return str(path+filename)



def pack_menu(menu):
	st='{"menus":['
	for dish in menu:
		st += json.dumps({
			"id": dish.id,
			"name": dish.name,
			'description': dish.description,
			'composition': dish.composition,
			'cost': float(dish.cost),
			'image': path+dish.image,
			'availability': dish.availability,
			'restourant_id': dish.restourant_id})
		st = st + ','
	st = st[:-1]
	st+=']}'
	#print(st)
	return st



def pack_restorant_list(Restourant):
	st= '{"value":['
	for i in Restourant:
		#data = {}
		#f= open('C:/android_projects/delcibo/back1/delcibo/app/static/images/logo.png', mode='rb')
		#img = f.read()
		#f.close()
		#data['img'] = base64.encodebytes(img).decode("utf-8")

		st = st+json.dumps({
			"id":i.id,
			"name": i.name,
			'description':i.description,
			'phone':i.phone,
			'address':i.address,
			'rating':i.rating,
			'email':i.email,
			'cost':i.cost,
			'icon':get_path(i.icon)})
			#'gallery':json.dumps(data)})
		st=st+','
	#st=st+json.dumps({'theEnd':'end'})
	st=st[:-1]+']}'
	return st

def pack_restorant(rest):
	tempg = '"gallery":['
	for gal in rest.gallery:
		tempg+= '{"url":"' + get_path(str(gal.path))+'"},'
	tempg = tempg[:-1]
	tempg+='],'
	tempm = '"menu":['
	for menu in rest.menu:
		tempm+= '{"id":' + str(menu.id)+','
		tempm += '"name":"' + str(menu.name) + '",'
		tempm+= '"description":"' + str(menu.description)+'",'
		tempm+= '"composition":"' + str(menu.composition)+'",'
		tempm+= '"image":"' + get_path(str(menu.image))+'",'
		tempm+= '"cost":' + str(menu.cost)+'},'
	tempm = tempm[:-1]
	tempm+=']'

	st = json.dumps({

	"id":rest.id,
	"name": rest.name,
	'description':rest.description,
	'phone':rest.phone,
	'address':rest.address,
	'rating':rest.rating,
	'email':rest.email,
	'cost':rest.cost})
			#'gallery':json.dumps(data)})
	st=st[:-1]+', '+tempg
	st+=tempm
	st+='}'
	return  (st)

def pack_places(Places):
	json = '{"image":"'+ get_path(str(Places.image)) + '", '

	json += str(Places.bisy_places)+'}'
	return json



def pack_restorant_for_admin(rest):
	tempg = '"gallery":['
	i=0
	tempg += '{"url":" "},'
	for gal in rest.gallery:
		i=1
		tempg += '{"url":"' + get_path(str(gal.path)) + '"},'
	tempg = tempg[:-1]
	tempg += ']'
	st = json.dumps({

		"id": rest.id,
		"name": rest.name,
		'description': rest.description,
		'icon': get_path(rest.icon),
		'phone': rest.phone,
		'address': rest.address,
		'rating': rest.rating,
		'email': rest.email,
		'kitchenType':rest.kitchenType,
		'restourantType':rest.restourantType,
		'password':rest.password,
		'www': rest.www,
		'time': rest.time,
		'all': rest.all,

		'cost': rest.cost})
	# 'gallery':json.dumps(data)})

	if i==1: st = st[:-1] + ', ' + tempg
	else: st = st = st[:-1]

	st += '}'
	return (st)





def buildRandomString(size):
    return ''.join(random.choice(string.ascii_letters) for _ in range(size))


def create_image_from_base64(baseString):
	fileName = buildRandomString(30)
	fileName+=".png"
	imgdata = base64.b64decode(baseString)


	with open(root + fileName, 'wb') as f:
		f.write(imgdata)

	return str(fileName)

def pack_halls(Halls):
	tempg = '{"halls":['
	temp = ''
	for i in range(len(Halls)):
		temp += '{"id":'+str(Halls[i].id)+','+'"name":"'+Halls[i].name+'",'+'"count":'+str(Halls[i].count)+','+'"image":"'+ get_path(str(Halls[i].image))+'"},'
	temp = temp[:-1]
	temp = tempg + temp + ']}'

	return temp

def pack_busy_places(places):
	tempg = '{"places":['
	temp = ''
	for i in range(len(places)):
		temp += '{"id_key":"'+str(places[i].id_key)+'",'+'"status":"'+places[i].status+'"},'
	temp = temp[:-1]
	temp = tempg + temp + ']}'

	return temp


def pack_week(week):
	if week!=None:
		json = '{"week":['
		json+='{ "name":"Monday",' \
			  + '"timestart":'+'"' + week.Monday_start+'",' \
			+ '"timestop":'+'"' + week.Monday_stop+'"},'
		json+='{ "name":"Tuesday",' \
			  + '"timestart":'+'"' + week.Tuesday_start+'",' \
			+ '"timestop":'+'"' + week.Thursday_stop+'"},'
		json+='{ "name":"Wednesday",' \
			  + '"timestart":'+'"' + week.Wednesday_start+'",' \
			+ '"timestop":'+'"' + week.Wednesday_stop+'"},'
		json+='{ "name":"Thursday",' \
			  + '"timestart":'+'"' + week.Thursday_start+'",' \
			+ '"timestop":'+'"' + week.Thursday_stop+'"},'
		json+='{ "name":"Friday",' \
			  + '"timestart":'+'"' + week.Friday_start+'",' \
			+ '"timestop":'+'"' + week.Friday_stop+'"},'
		json+='{ "name":"Saturday",' \
			  + '"timestart":'+'"' + week.Saturday_start+'",' \
			+ '"timestop":'+'"' + week.Saturday_stop+'"},'
		json+='{ "name":"Sunday",' \
			  + '"timestart":'+'"' + week.Sunday_start+'",' \
			+ '"timestop":'+'"' + week.Sunday_stop+'"}]'
		if str(week.datetime).find('SELECT') == -1: return json+'}'
		else:

			json+=', "all":['
			for datatime in week.datetime:
				json+='{"name":"'+datatime.date+'",'+'"timestart":"'+datatime.timeStart+'",'+'"timestop":"'+datatime.timeStop+'"},'
			json = json[:-1]
			return json+']}'
	else: return "None"


