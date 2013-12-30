#!/usr/bin/env python
# encoding: utf-8
"""
profile.py

Created by Aparna Bhat,Kiran on 2013-12-28.
Copyright (c) 2013 __Corneus__. All rights reserved.
"""
from pyramid.view import view_config
import json
import urlparse
from pyramid.httpexceptions import *

@view_config(route_name='self_profile', renderer='neuron:templates/self_profile.mako')
def load_self_profile(request):
	session=request.session
	uname=session['name']
	collection_details=request.db['users']
	user=collection_details.find_one({'username':uname})
	f_name=user["first_name"]
	l_name=user["last_name"]
	return{'f_name':f_name,'l_name':l_name}
	
	
@view_config(route_name='view_friends', renderer='neuron:templates/view_friends.mako')
def view_friends(request):
	session=request.session
	uname=session['name']
	collection_details=request.db['users']
	user=collection_details.find_one({'username':uname})
	f_name=user["first_name"]
	l_name=user["last_name"]
	return{'f_name':f_name,'l_name':l_name}
	
	



