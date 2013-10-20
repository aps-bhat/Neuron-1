from pyramid.view import view_config
from neuron.utilities.authen import Authen
from neuron.utilities.register import RegisterUser
from neuron.utilities.prof_pic import ProfilePicture
from neuron.utilities.resume import Resume
from velruse import login_url
import json
import logging
import os
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

def session_check(request):
    session=request.session
    return {'session':session['name']}

def register_profiledetails(request):
    session=request.session
    fname=request.params["fname"]
    lname=request.params["lname"]
    date=request.params["date"]
    month=request.params["month"]
    year=request.params["year"]
    city=request.params["ccity"]
    designation=request.params["designation"]
    #print(session['name'],fname,lname,date,month,year,city,designation)
    return {'username':'appu', 'password':'appu', 'state': 'successful'}

def signup(request):
    return { 'page': 'SIGN UP!!!!'}

def register_user(request):
    username=request.params["uname"]
    password=request.params["pword"]
    email=request.params["email"]
    fname=request.params["fname"]
    lname=request.params["lname"]
    WriteUser= RegisterUser(request)
    WriteUser.EnterUser(username,password,email,fname,lname)
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
    tmp=project_home+"/login/static/images/"
    session=request.session
    username=session['name']
    tmp = tmp + username
    if not os.path.exists(tmp):
        os.makedirs(tmp)
    tmp= tmp + "/img0.jpeg"
    output=open(tmp, 'w')
    output.write(input_file.read())
    output.close()
    ppobj=ProfilePicture(request)
    ppobj.EnterFirstProfPic(username)
    return { 'username':username, 'password':'password', 'state':'saved','session':session['name']}

def login_complete_view(request):
    context = request.context
    result = {
        'profile': context.profile,
        'credentials': context.credentials,
    }
    #print(result['profile']['accounts'])
    account=result['profile']['accounts']
    domain=account[0]['domain']
    if(domain=="facebook.com"):
        username=result['profile']['preferredUsername']
        setting = request.registry.settings
        collection = request.db['users']
        flag_to_insert=collection.find_one({'username':username})
        if not flag_to_insert:
            user={'username':username, 'email_id':result['profile']['verifiedEmail']}
            collection.insert(user)
    if(domain=="twitter.com"):
        username=result['profile']['displayName']
        setting = request.registry.settings
        collection = request.db['users']
        flag_to_insert=collection.find_one({'username':username})
        if not flag_to_insert:
            user={'username':username}
            collection.insert(user)
        
   #print(result['profile']['displayName'])
    return {
        'result': json.dumps(result, indent=4)
    }

