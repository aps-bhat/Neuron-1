from pyramid.view import view_config
from neuron.utilities.authen import Authen
from neuron.utilities.register import RegisterUser
from neuron.utilities.prof_pic import ProfilePicture
from neuron.utilities.resume import Resume
from velruse import login_url
import json
import logging
import os
from pyramid.httpexceptions import *
def index(request):
    return {'page':'login', 'state':'Please SIGN IN !!!'}

#@view_config(route_name='auth', renderer='login:templates/auth.pt')
def authenticate(request):
    username=request.params["uname"]
    password=request.params["pword"]
    Userdata=Authen(request)
    session=request.session
    if(Userdata.CheckUser(username,password)):
       session['name']=username
       session.save()
       return {'username':username, 'password':password, 'state': 'successful','session':session['name']}
    else:
        session.invalidate()
        return {'username':username, 'password':password, 'state': 'try again','session':'empty'}


def register_profiledetails(request):
    session=request.session
    username=session['name']
    fname=request.params["fname"]
    lname=request.params["lname"]
    date=request.params["date"]
    month=request.params["month"]
    year=request.params["year"]
    city=request.params["ccity"]
    designation=request.params["designation"]
    #print(session['name'],fname,lname,date,month,year,city,designation)
    UpdateUser=RegisterUser(request)
    UpdateUser.EnterUserDetails(username,fname,lname,date,month,year,city,designation)
    return {'username':'appu', 'password':'appu', 'state': 'successful'}

def signup(request):
    return { 'page': 'SIGN UP!!!!'}

def register_user(request):
    username=request.params["uname"]
    password=request.params["pword"]
    email=request.params["email"]
    #fname=request.params["fname"]
    #lname=request.params["lname"]
    WriteUser= RegisterUser(request)
    n=WriteUser.EnterUser(request,username,password,email)
    if(n==1):
		return HTTPFound(location=request.route_url('sign-up'))
    session=request.session
    session['name']=username
    session.save()
    return {'username':username, 'password':password, 'state': 'successful'}

def login_view(request):
    return {
        'login_url': login_url,
        'providers': request.registry.settings['login_providers'],
    }

def process_profile_picture(request):
    input_file=request.POST["prof_pic"].file
    project_home=os.environ['PROJECT_HOME']
    tmp=project_home+"/neuron/static/images/"
    session=request.session
    username=session['name']
    tmp = tmp + username+"/profile_pictures"
    if not os.path.exists(tmp):
        os.makedirs(tmp)
    tmp= tmp + "/img0.jpeg"
    output=open(tmp, 'w')
    output.write(input_file.read())
    output.close()
    ppobj=ProfilePicture(request)
    ppobj.EnterFirstProfPic(username)
    return { 'username':username, 'password':'password', 'state':'saved','session':session['name']}

def error(request):
	return {}
	
def social(request):
	session=request.session
	username=session['name']
	return { 'username':username, 'password':'password', 'state':'saved','session':session['name']}
	
def login_complete_view(request):
    context = request.context
	#retrieving the social profile details of the user
    result = {
        'profile': context.profile,
        'credentials': context.credentials,
    }
	#retrieving the domain of the social network
    account=result['profile']['accounts']
    domain=account[0]['domain']
    if(domain=="facebook.com"):
        username=result['profile']['preferredUsername'] #retrieve username from the social profile
        setting = request.registry.settings
        collection = request.db['users']
        flag_to_insert=collection.find_one({'username':username}) 
		#check if username is already available in the table or not if not insert it
        if not flag_to_insert:
            user={'username':username, 'email_id':result['profile']['verifiedEmail'],'social_domain':'facebook'}
            collection.insert(user)
            session=request.session
            session['name']=username
            return HTTPFound(location=request.route_url('social_first'))
		#If user name is already available in the table, check domain name matches to facebook, if not redirect to sign up page else login in by setting session
        else:
            social=flag_to_insert['social_domain']
            if(social=="facebook"):
                session=request.session
                session['name']=username
                return HTTPFound(location=request.route_url('social'))
            else:
                return HTTPFound(location=request.route_url('sign-up'))
    if(domain=="twitter.com"):
        username=account[0]['username'] #retrieve username from the social profile
        setting = request.registry.settings
        collection = request.db['users']
        flag_to_insert=collection.find_one({'username':username})
		#check if username is already available in the table or not if not insert it
        if not flag_to_insert:
            user={'username':username,'social_domain':'twitter'}
            collection.insert(user)
            session=request.session
            session['name']=username
            return HTTPFound(location=request.route_url('social_first'))
		#If user name is already available in the table, check domain name matches to twitter, if not redirect to sign up page else login in by setting session
        else:
            social=flag_to_insert['social_domain']
            if(social=="twitter"):
                session=request.session
                session['name']=username
                return HTTPFound(location=request.route_url('social'))
            else:
                return HTTPFound(location=request.route_url('sign-up'))
    

