from pyramid.view import view_config
from neuron.utilities.authen import Authen
from neuron.utilities.register import RegisterUser
from neuron.utilities.prof_pic import ProfilePicture
from neuron.utilities.resume import Resume
from velruse import login_url
import json
import logging
import os

def resume_read(request):
    session=request.session
    uname=session['name']
    resobj=Resume(request)
    res_dic=resobj.resumeread(uname)
    return res_dic

def resume_write(request):
    setting=request.registry.settings
    session=request.session
    uname=session['name']
    collection_resume=request.db['resume']
    person=collection_resume.find_one({'username':uname})
    collection_schoolid=request.db['resume_misc']
    schools=[]
    name=[]
    d_o_j=[]
    d_o_l=[]
    place=[]
    m_s=[]
    o_f=[]
    try:
        schools=person['school']
    except TypeError:
        schools=[]
    no_of_p=request.params['p_tag']
    Address=request.params["address"]
    collection_school=request.db['school']
    for i in range(0,int(no_of_p)):
        flag=0
        sch=collection_schoolid.find_one({'name':'sid'})
        school_count=int(sch["value"])
        if not school_count:
            school_count=0
        name.append(request.params['name_school_'+str(i)])
        d_o_j.append(request.params['doj_school_'+str(i)])
        d_o_l.append(request.params['dol_school_'+str(i)])
        place.append(request.params['city_school_'+str(i)])
        m_s.append(request.params['ms_school_'+str(i)])
        o_f.append(request.params['outof_school_'+str(i)])
        try: 
            temp=schools[i]
        except IndexError:
            schools.append(school_count+1)
            flag=1
        collection_school.update({'sid':schools[i]},{"$set":{'name':name[i],'date_of_joining':d_o_j[i],'date_of_leaving':d_o_l[i],'place':place[i],
        'marks_secured':m_s[i],'out_of':o_f[i]}},upsert=True)
        if(flag==1):
           collection_schoolid.update({'name':'sid'},{"$set":{'value':school_count+1}})
    collection_resume.update({'username':uname},{"$set":{'address':Address,'school':schools}},upsert=True)
    return {'address':Address,'username':uname,'no_of_p':no_of_p,'name':name,'d_o_j':d_o_j,'d_o_l':d_o_l,'place':place,'m_s':m_s,'o_f':o_f}
    
def resume_delete(request):
    setting=request.registry.settings
    session=request.session
    uname=session['name']
    collection_resume=request.db['resume']
    collection_school=request.db['school']
    person=collection_resume.find_one({'username':uname})
    d=request.params["del"]
    d=d.split("_")
    print d[0],d[1]
    val=d[0]
    no=int(d[1])
    if(val=="sch"):
         school=person["school"]
         print school
         sc=school[no]
         del school[no]
         print school
         collection_resume.update({'username':uname},{"$set":{'school':school}})
         collection_school.remove({'sid':sc})
    resobj=Resume(request)
    res_dic=resobj.resumeread(uname)
    return res_dic

