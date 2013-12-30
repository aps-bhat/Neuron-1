from pyramid.view import view_config
from neuron.utilities.authen import Authen
from neuron.utilities.register import RegisterUser
from neuron.utilities.prof_pic import ProfilePicture
from neuron.utilities.resume import Resume
from velruse import login_url
import json
import logging
import os
import urlparse
from pyramid.httpexceptions import *

@view_config(renderer="json",name="addpursuer.json")
def addpursuing(request):
	session=request.session
	uname=session['name']
	username=str(uname)
	url=request.url
	parsed=urlparse.urlparse(url)
	friend_name=urlparse.parse_qs(parsed.query)['Pursuing']
	friend=friend_name[0]
	collection_friend=request.db["friends"]
	friends=collection_friend.find_one({'username':username})
	pursuing=friends['pursuing']
	no_of_pursuing=int(friends['no_pursuing'])
	no_of_pursuing=no_of_pursuing+1
	pursuing.append(friend)
	collection_friend.update({'username':username},{"$set":{'pursuing':pursuing,'no_pursuing':no_of_pursuing}})
	pursuers=friends['pursuers']
	if friend in pursuers:
		mutual=friends['mutual']
		no_of_mutual=int(friends['no_mutual'])
		no_of_mutual=no_of_mutual+1
		mutual.append(friend)
		collection_friend.update({'username':username},{"$set":{'mutual':mutual,'no_mutual':no_of_mutual}})
		friends=collection_friend.find_one({'username':friend})
		no_of_mutual=int(friends['no_mutual'])
		no_of_mutual=no_of_mutual+1
		mutual=friends['mutual']
		mutual.append(username)
		collection_friend.update({'username':friend},{"$set":{'mutual':mutual,'no_mutual':no_of_mutual}})
	friends=collection_friend.find_one({'username':friend})
	pursuers=friends['pursuers']
	no_of_pursuers=int(friends['no_pursuers'])
	no_of_pursuers=no_of_pursuers+1
	pursuers.append(username)
	collection_friend.update({'username':friend},{"$set":{'pursuers':pursuers,'no_pursuers':no_of_pursuers}})
	return {'state':'success'}

                                                                #purpose: To check if the user is already pursuing a third person friend
@view_config(renderer="json",name="checkpursuing.json")
def check_pursuing_function(request):
	session=request.session                    				    #getting username from the session
	uname=session['name']
	url=request.url 											#getting friend's name from the JSON object passed from templates/friend.mako
	parsed=urlparse.urlparse(url)
	friend_name=urlparse.parse_qs(parsed.query)['Pursuing']
	friend=friend_name[0] 										#storing the name of friend in friend object
	collection_friend=request.db["friends"] 					#Creating an object for the friends database
	friends=collection_friend.find_one({'username':uname})	    #finding the record corresponding to user
	pursuing=friends['pursuing']                                # Obtaining the value of the pursuing field
	if friend in pursuing:                                      #if user is already pursuing a person, we return true. Else we return false
		return {'state':'true'}
	else:
		return {'state':'false'}
	
@view_config(renderer="json",name="removepursuer.json")
def removepursuing(request):
	session=request.session 									#getting username from the session
	username=session['name']
	url=request.url												#getting friend's name from the JSON object passed from templates/friend.mako
	parsed=urlparse.urlparse(url)
	friend_name=urlparse.parse_qs(parsed.query)['Pursuing']
	friend=friend_name[0]
	collection_friend=request.db['friends']
	friends=collection_friend.find_one({'username':username})
	pursuing=friends['pursuing']
	no_of_pursuing=int(friends['no_pursuing'])
	no_of_pursuing=no_of_pursuing-1
	pursuing.remove(friend)
	collection_friend.update({'username':username},{"$set":{'pursuing':pursuing,'no_pursuing':no_of_pursuing}})
	pursuers=friends['pursuers']
	if friend in pursuers:
		mutual=friends['mutual']
		no_of_mutual=int(friends['no_mutual'])
		no_of_mutual=no_of_mutual-1
		mutual.remove(friend)
		collection_friend.update({'username':username},{"$set":{'mutual':mutual,'no_mutual':no_of_mutual}})
		friends=collection_friend.find_one({'username':friend})
		no_of_mutual=int(friends['no_mutual'])
		no_of_mutual=no_of_mutual-1
		mutual=friends['mutual']
		mutual.remove(username)
		collection_friend.update({'username':friend},{"$set":{'mutual':mutual,'no_mutual':no_of_mutual}})
	friends=collection_friend.find_one({'username':friend})
	pursuers=friends['pursuers']
	no_of_pursuers=int(friends['no_pursuers'])
	no_of_pursuers=no_of_pursuers-1
	pursuers.remove(username)
	collection_friend.update({'username':friend},{"$set":{'pursuers':pursuers,'no_pursuers':no_of_pursuers}})
	return {'state':'success'}

@view_config(renderer="json",name="viewpursuing.json")
def viewpursuing(request):
	session=request.session
	username=session['name']
	collection_pursuing=request.db['friends']
	collection_users=request.db['search_users']
	friends=collection_pursuing.find_one({'username':username})
	pursuing=friends['pursuing']
	to_return={}
	for person in pursuing:
		user_details=collection_users.find_one({'username':person})
		uname=user_details['username']
		picloc=user_details['piclocation']
		to_return[uname]=picloc
	return to_return

@view_config(renderer="json",name="viewmutual.json")
def viewmutual(request):
	session=request.session
	username=session['name']
	collection_pursuing=request.db['friends']
	collection_users=request.db['search_users']
	friends=collection_pursuing.find_one({'username':username})
	pursuing=friends['mutual']
	to_return={}
	for person in pursuing:
		user_details=collection_users.find_one({'username':person})
		uname=user_details['username']
		picloc=user_details['piclocation']
		to_return[uname]=picloc
	return to_return

@view_config(renderer="json",name="viewpursuers.json")
def viewpursuers(request):
	session=request.session
	username=session['name']
	collection_pursuing=request.db['friends']
	collection_users=request.db['search_users']
	friends=collection_pursuing.find_one({'username':username})
	pursuing=friends['pursuers']
	to_return={}
	for person in pursuing:
		user_details=collection_users.find_one({'username':person})
		uname=user_details['username']
		picloc=user_details['piclocation']
		to_return[uname]=picloc
	return to_return