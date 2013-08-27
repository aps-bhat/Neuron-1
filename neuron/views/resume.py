#should be optimized and documented
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
    except KeyError:
        schools=[]
    no_of_p=request.params['p_tag']
    Address=request.params["address"]
    #print no_of_p
    collection_school=request.db['school_set']
    collection_indv_school=request.db['school']
    for i in range(0,int(no_of_p)):
        flag=0
        sch=collection_schoolid.find_one({'name':'sid'})
        school_count=int(sch["value"])
        name.append(request.params['name_school_'+str(i)])
        d_o_j.append(request.params['doj_school_'+str(i)])
        d_o_l.append(request.params['dol_school_'+str(i)])
        place.append(request.params['city_school_'+str(i)])
        m_s.append(request.params['ms_school_'+str(i)])
        o_f.append(request.params['outof_school_'+str(i)])
        try:
           temp=schools[i] #the skill already exists 
           school_exists=collection_school.find_one({'name_of_school':name[i]}) #obtaining the corresponding sk_id
           schid=school_exists["schid"]
           count_students=int(school_exists["count_students"])
           #print i,'Inside try ',sk_id
        except IndexError: #the skill does not exist
           try: #getting the value of sk_id
             school_exists=collection_school.find_one({'name_of_school':name[i]}) #finding if the skill is already present
             schid=school_exists["schid"] #getting the sk_id for storing it
             count_students=int(school_exists["count_students"])
           except KeyError:
             sch_id=collection_schoolid.find_one({'name':'schid'}) #inserting that skill into the skill_set table
             schid=int(sch_id["value"])+1
             collection_school.insert({'schid':schid,'name_of_school':name[i],'place':place[i]})
             collection_schoolid.update({'name':'schid'},{"$set":{'value':schid}})
             count_students=0
           except TypeError:
             sch_id=collection_schoolid.find_one({'name':'schid'}) #inserting that skill into the skill_set table
             schid=int(sch_id["value"])+1
             collection_school.insert({'schid':schid,'name_of_school':name[i],'place':place[i]})
             collection_schoolid.update({'name':'schid'},{"$set":{'value':schid}})
             count_students=0
           school_count=school_count+1  
           schools.append(school_count)  
           count_students=count_students+1
           collection_school.update({'schid':schid},{"$set":{'count_students':count_students}})
        collection_schoolid.update({'name':'sid'},{"$set":{'value':school_count}})
        collection_indv_school.update({'sid':schools[i]},{"$set":{'schid':schid,'date_of_joining':d_o_j[i],'date_of_leaving':d_o_l[i],
        'marks_secured':m_s[i],'out_of':o_f[i]}},upsert=True)
    collection_resume.update({'username':uname},{"$set":{'address':Address,'school':schools}},upsert=True)
    colleges=[]
    degree=[]
    course=[]
    name_coll=[]
    place_coll=[]
    d_o_j_coll=[]
    d_o_l_coll=[]
    m_s_coll=[]
    o_f_coll=[]
    no_of_pc=0 
    colid=0 #college_p_tag
    count_students=0
    try:
        colleges=person['college']
    except KeyError:
        colleges=[]
    except TypeError:
        colleges=[]
    no_of_pc=request.params['no_of_pc']
    collection_college=request.db['college_set']
    collection_indv_college=request.db['graduate']
    for i in range(0,int(no_of_pc)):
        flag=0
        cch=collection_schoolid.find_one({'name':'cid'})
        college_count=int(cch["value"])
        degree.append(request.params['degree_college_'+str(i)])
        course.append(request.params['course_college_'+str(i)])
        name_coll.append(request.params['name_college_'+str(i)])
        place_coll.append(request.params['city_college_'+str(i)])
        d_o_j_coll.append(request.params['doj_college_'+str(i)])
        d_o_l_coll.append(request.params['dol_college_'+str(i)])
        m_s_coll.append(request.params['ms_college_'+str(i)])
        o_f_coll.append(request.params['outof_college_'+str(i)]) 
        try:
           temp=colleges[i] #the skill already exists 
           college_exists=collection_college.find_one({'name_of_college':name_coll[i],'place':place_coll[i]}) #obtaining the corresponding sk_id
           colid=college_exists["colid"]
           
           count_students=int(college_exists["count_students"])
           #print i,'Inside try ',sk_id
        except IndexError: #the skill does not exist
           try: #getting the value of sk_id
             college_exists=collection_college.find_one({'name_of_college':name_coll[i]}) #finding if the skill is already present
             col_id=college_exists["colid"] #getting the sk_id for storing it
             count_students=int(college_exists["count_students"])
           except KeyError:
             col_id=collection_schoolid.find_one({'name':'colid'}) #inserting that skill into the skill_set table
             colid=int(col_id["value"])+1
             collection_college.insert({'colid':colid,'name_of_college':name_coll[i],'place':place_coll[i]})
             collection_schoolid.update({'name':'colid'},{"$set":{'value':colid}})
             count_students=0
           except TypeError:
             col_id=collection_schoolid.find_one({'name':'colid'}) #inserting that skill into the skill_set table
             colid=int(col_id["value"])+1
             collection_college.insert({'colid':colid,'name_of_college':name_coll[i],'place':place_coll[i]})
             collection_schoolid.update({'name':'colid'},{"$set":{'value':colid}})
             count_students=0
           college_count=college_count+1  
           colleges.append(college_count)  
           count_students=count_students+1
           collection_college.update({'colid':colid},{"$set":{'count_students':count_students}})
        collection_schoolid.update({'name':'cid'},{"$set":{'value':college_count}})
        #print colid
        collection_indv_college.update({'gid':colleges[i]},{"$set":{'colid':colid,'degree':degree[i],'course':course[i],'date_of_joining':d_o_j_coll[i],'date_of_leaving':d_o_l_coll[i],'marks_secured':m_s_coll[i],'out_of':o_f_coll[i]}},upsert=True)
    collection_resume.update({'username':uname},{"$set":{'address':Address,'college':colleges}},upsert=True)  
    projects=[]
    pro_title=[]
    pro_description=[]
    pro_members=[]
    pro_publications=[]
    pro_from=[]
    pro_to=[]
    pro_links=[]
    no_of_pro=0  #project_p_tag
    try:
        projects=person['project']
    except KeyError:
        projects=[]
    except TypeError:
        projects=[]
    no_of_pro=request.params['no_of_pro'] #project_p_tag
    collection_project=request.db['project']
    for i in range(0,int(no_of_pro)):
        flag=0
        pch=collection_schoolid.find_one({'name':'pid'})
        project_count=int(pch["value"])
        if not project_count:
            project_count=0
        pro_title.append(request.params['project_title_'+str(i)])
        pro_description.append(request.params['project_desc_'+str(i)])
        pro_members.append(request.params['project_mem_'+str(i)])
        pro_publications.append(request.params['project_pub_'+str(i)])
        pro_from.append(request.params['project_from_'+str(i)])
        pro_to.append(request.params['project_to_'+str(i)])
        pro_links.append(request.params['project_link_'+str(i)])
        collection_project.update({'pid':projects[i]},{"$set":{'title':pro_title[i],'description':pro_description[i],'members':pro_members[i],'publications':pro_publications[i],'from':pro_from[i],'to':pro_to[i],'links':pro_links[i]}},upsert=True)
        if(flag==1):
           collection_schoolid.update({'name':'pid'},{"$set":{'value':project_count+1}})
    collection_resume.update({'username':uname},{"$set":{'project':projects}},upsert=True)
    employments=[]
    name_company=[]
    place_company=[]
    from_company=[]
    to_company=[]
    pos_company=[]
    no_of_emp=0  #employment_p_tag
    try:
        employments=person['employment']
    except KeyError:
        employments=[]
    except TypeError:
        employments=[]
    no_of_emp=request.params['no_of_emp'] #project_p_tag
    collection_indv_employment=request.db['employment']
    collection_employment=request.db['employment_set']
    for i in range(0,int(no_of_emp)):
        name_company.append(request.params['name_company_'+str(i)])
        place_company.append(request.params['place_company_'+str(i)])
        from_company.append(request.params['from_company_'+str(i)])
        to_company.append(request.params['to_company_'+str(i)])
        pos_company.append(request.params['pos_company_'+str(i)])
        ech=collection_schoolid.find_one({'name':'eid'})
        employment_count=int(ech["value"])
        try:
           temp=employments[i] #the skill already exists 
           employment_exists=collection_employment.find_one({'name_of_company':name_company[i],'place':place_company[i]}) #obtaining the corresponding sk_id
           cmp_id=employment_exists["cmpid"]
           count_employee=int(employment_exists["count_employment"])
           #print i,'Inside try ',sk_id
        except IndexError: #the skill does not exist
           try: #getting the value of sk_id
             employment_exists=collection_employment.find_one({'name_of_company':name_company[i]}) #finding if the skill is already present
             cmp_id=employment_exists["cmpid"] #getting the sk_id for storing it
             count_employee=int(employment_exists["count_employment"])
           except KeyError:
             cmpid=collection_schoolid.find_one({'name':'cmpid'}) #inserting that skill into the skill_set table
             cmp_id=int(cmpid["value"])+1
             collection_employment.insert({'cmpid':cmp_id,'name_of_company':name_company[i],'place':place_company[i]})
             collection_schoolid.update({'name':'cmpid'},{"$set":{'value':cmp_id}})
             count_employee=0
           except TypeError:
             cmpid=collection_schoolid.find_one({'name':'cmpid'}) #inserting that skill into the skill_set table
             cmp_id=int(cmpid["value"])+1
             collection_employment.insert({'cmpid':cmp_id,'name_of_company':name_company[i],'place':place_company[i]})
             collection_schoolid.update({'name':'cmpid'},{"$set":{'value':cmp_id}})
             count_employee=0
           employment_count=employment_count+1  
           employments.append(employment_count)  
           count_employee=count_employee+1
           collection_employment.update({'cmpid':cmp_id},{"$set":{'count_employment':count_employee}})
        collection_schoolid.update({'name':'eid'},{"$set":{'value':employment_count}})
        collection_indv_employment.update({'eid':employments[i]},{"$set":{'cmpid':cmp_id,'from':from_company[i],'to':to_company[i],'position':pos_company[i]}},upsert=True)
    collection_resume.update({'username':uname},{"$set":{'employment':employments}},upsert=True)  
    #skills 
    name_of_skills=[] # Tha variables used to store value from the previous page
    endorsed=[]
    skills=[]
    level_skill=[]
    no_of_skill=0
    sk_id=0
    skl_id=0
    try:
        skills=person['skill'] #obtaining the existing value stored in the resume table
    except KeyError:
        skills=[]
    except TypeError:
        skills=[]
    coll=request.db["resume_misc"]
    no_of_skill=request.params['no_of_skill']
    collection_skill=request.db['skill_set'] #the skill_set table
    collection_indv_skill=request.db['skill'] #the skill of the person table
    for i in range (0,int(no_of_skill)):
       name_of_skills.append(request.params['name_skill_'+str(i)]) #obtaining the skills from the page to display them again
       level_skill.append(request.params['level_skill_'+str(i)])
       skill_inv=coll.find_one({'name':'skillid'}) # error in retriving this part.. value is 0.. check console
       skl_id=int(skill_inv["value"])
       try:
           temp=skills[i] #the skill already exists 
           skill_excists=collection_skill.find_one({'name_of_skill':name_of_skills[i]}) #obtaining the corresponding sk_id
           sk_id=skill_excists["skid"]
           count_skill=int(skill_excists["count_skill"])
           #print i,'Inside try ',sk_id
       except IndexError: #the skill does not exist
           try: #getting the value of sk_id
             skill_excists=collection_skill.find_one({'name_of_skill':name_of_skills[i]}) #finding if the skill is already present
             sk_id=skill_excists["skid"] #getting the sk_id for storing it
             count_skill=int(skill_excists["count_skill"])
           except KeyError:
             sklid=collection_schoolid.find_one({'name':'skid'}) #inserting that skill into the skill_set table
             sk_id=int(sklid["value"])+1
             collection_skill.insert({'skid':sk_id,'name_of_skill':name_of_skills[i]})
             collection_schoolid.update({'name':'skid'},{"$set":{'value':sk_id}})
             count_skill=0
           except TypeError:
             sklid=collection_schoolid.find_one({'name':'skid'}) #inserting that skill into the skill_set table
             sk_id=int(sklid["value"])+1
             collection_skill.insert({'skid':sk_id,'name_of_skill':name_of_skills[i]})
             collection_schoolid.update({'name':'skid'},{"$set":{'value':sk_id}})
             count_skill=0
           skl_id=skl_id+1  
           skills.append(skl_id)  
           count_skill=count_skill+1
           collection_skill.update({'name':'skid'},{"$set":{'count_skill':count_skill}})
       collection_indv_skill.update({'skl_id':skills[i]},{"$set":{'sk_id':sk_id,'level_skill':level_skill[i]}},upsert=True)
       collection_schoolid.update({'name':'skillid'},{"$set":{'value':skl_id}})
    collection_resume.update({'username':uname},{"$set":{'skill':skills}},upsert=True)  
    return {'address':Address,'username':uname,'no_of_p':no_of_p,'name':name,'d_o_j':d_o_j,'d_o_l':d_o_l,'place':place,'m_s':m_s,'o_f':o_f,
    'no_of_pc':no_of_pc,'degree':degree,'course':course,'name_coll':name_coll,'place_coll':place_coll,'d_o_j_coll':d_o_j_coll,'d_o_l_coll':d_o_l_coll,
    'm_s_coll':m_s_coll,'o_f_coll':o_f_coll,'no_of_pro':no_of_pro,'project_title':pro_title,'project_desc':pro_description,'project_mem':pro_members,      'project_pub':pro_publications,'project_from':pro_from,'project_to':pro_to,'project_link':pro_links,'name_company':name_company,'place_company':place_company,
    'from_company':from_company,'to_company':to_company,'pos_company':pos_company,'no_of_emp':no_of_emp,'no_of_skill':no_of_skill,'name_skill':name_of_skills,'level_skill':level_skill}

def resume_delete(request):
    setting=request.registry.settings
    session=request.session
    uname=session['name']
    collection_resume=request.db['resume']
    collection_school=request.db['school']
    collection_college=request.db['graduate']
    collection_project=request.db['project']
    collection_employment=request.db['employment']
    person=collection_resume.find_one({'username':uname})
    d=request.params["del"]
    d=d.split("_")
    #print d[0],d[1]
    val=d[0]
    no=int(d[1])
    if(val=="sch"):
         school=person["school"]
         #print school
         sc=school[no]
         del school[no]
         #print school
         collection_resume.update({'username':uname},{"$set":{'school':school}})
         collection_school.remove({'sid':sc})
    if(val=="cch"):
        college=person["college"]
        cc=college[no]
        del college[no]
        collection_resume.update({'username':uname},{"$set":{'college':college}})
        collection_college.remove({'gid':cc})
    if(val=="pch"):
        project=person["project"]
        pc=project[no]
        del project[no]
        collection_resume.update({'username':uname},{"$set":{'project':project}})
        collection_project.remove({'pid':pc})
    if(val=="ech"):
        employment=person["employment"]
        ec=employment[no]
        del employment[no]
        collection_resume.update({'username':uname},{"$set":{'employment':employment}})
        collection_employment.remove({'eid':ec})
    resobj=Resume(request)
    res_dic=resobj.resumeread(uname)
    return res_dic

