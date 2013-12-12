class Resume(object):
  def __init__(self,request):
     self.settings = request.registry.settings
     self.collection = request.db['resume']
     self.collection_school=request.db['school']
     self.collection_college=request.db['graduate']
     self.collection_project=request.db['project']
     self.collection_employment=request.db['employment']
     self.collection_skill_set=request.db['skill_set']
     self.collection_skill=request.db['skill']
     self.collection_school_set=request.db['school_set']
     self.collection_college_set=request.db['graduate_set']
     self.collection_employment_set=request.db['employment_set']
     self.collection_users=request.db['users']

  def resumeread(self,uname):
    user=self.collection_users.find_one({'username':uname})
    fname=user['first_name']
    lname=user['last_name']
    full_name=fname+" "+lname
    res=self.collection.find_one({'username':uname})
    #print res
    #check_address=Resume.get('address',None)
    try:
        Address=res['address']
    except TypeError:
        Address='Enter your address'
    except KeyError:
        Address='Enter your address'
    schools=[]
    colleges=[]
    name=[]
    d_o_j=[]
    d_o_l=[]
    place=[]
    m_s=[]
    o_f=[]
    no_of_p=0  #school_p_tag
    try:
        schools=res['school']
    except TypeError:
        schools=[]
    i=0
    for school in schools:
        school_detail=self.collection_school.find_one({'sid':school})
        schid=int(school_detail["schid"])
        sch_detail=self.collection_school_set.find_one({'schid':schid})
        name.append(sch_detail['name_of_school'])
        d_o_j.append(school_detail['date_of_joining'])
        d_o_l.append(school_detail['date_of_leaving'])
        place.append(sch_detail['place'])
        #print place
        m_s.append(school_detail['marks_secured'])
        o_f.append(school_detail['out_of'])
        i=i+1
    no_of_p=i;
    degree=[]
    course=[]
    name_coll=[]
    place_coll=[]
    d_o_j_coll=[]
    d_o_l_coll=[]
    project_ids=[]
    m_s_coll=[]
    o_f_coll=[]
    no_of_pc=0  #college_p_tag
    try:
        colleges=res['college']
    except KeyError:
        colleges=[]
    except TypeError:
        colleges=[]
    i=0
    for college in colleges:
        college_detail=self.collection_college.find_one({'gid':college})
        colid=int(college_detail["colid"])
        colg_detail=self.collection_college_set.find_one({'colid':colid})
        degree.append(college_detail['degree'])
        course.append(college_detail['course'])
        name_coll.append(colg_detail['name_of_college'])
        place_coll.append(colg_detail['place'])
        d_o_j_coll.append(college_detail['date_of_joining'])
        d_o_l_coll.append(college_detail['date_of_leaving'])
        m_s_coll.append(college_detail['marks_secured'])
        o_f_coll.append(college_detail['out_of'])
        i=i+1
    no_of_pc=i
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
        projects=res['project']
    except KeyError:
        projects=[]
    except TypeError:
        projects=[]
    i=0
    for project in projects:
        project_detail=self.collection_project.find_one({'pid':project})
        pro_title.append(project_detail['title'])
        pro_description.append(project_detail['description'])
        pro_members.append(project_detail['members'])
        pro_publications.append(project_detail['publications'])
        pro_from.append(project_detail['from'])
        pro_to.append(project_detail['to'])
        pro_links.append(project_detail['links'])
        i=i+1
    no_of_pro=i
    employments=[]
    name_company=[]
    place_company=[]
    from_company=[]
    to_company=[]
    pos_company=[]
    no_of_emp=0  #employment_p_tag
    try:
        employments=res['employment']
    except KeyError:
        employments=[]
    except TypeError:
        employments=[]
    i=0
    for employment in employments:
        employment_detail=self.collection_employment.find_one({'eid':employment})
        cmpid=int(employment_detail["cmpid"])
        emp_detail=self.collection_employment_set.find_one({'cmpid':cmpid})
        name_company.append(emp_detail['name_of_company'])
        place_company.append(emp_detail['place'])
        from_company.append(employment_detail['from'])
        to_company.append(employment_detail['to'])
        pos_company.append(employment_detail['position'])
        i=i+1
    no_of_emp=i
    #print no_of_emp
    skills=[]
    name_skill=[]
    level_skill=[]
    no_of_skill=0
    i=0
    try: 
        skills=res['skill']
    except KeyError:
        skills=[]
    except TypeError:
        skills=[]
    for skill in skills:
        skill_detail=self.collection_skill.find_one({'skl_id':skill})
        sk_id=int(skill_detail["sk_id"])
        name_of_skill_dict=self.collection_skill_set.find_one({'skid':sk_id})
        name_of_skill=name_of_skill_dict["name_of_skill"]
        name_skill.append(name_of_skill)
        level_skill.append(skill_detail["level_skill"])
        i=i+1
    no_of_skill=i
    return {'full_name':full_name,'address':Address,'username':uname,'no_of_p':no_of_p,'name':name,'d_o_j':d_o_j,'d_o_l':d_o_l,'place':place,'m_s':m_s,'o_f':o_f,
    'no_of_pc':no_of_pc,'degree':degree,'course':course,'name_coll':name_coll,'place_coll':place_coll,'d_o_j_coll':d_o_j_coll,'d_o_l_coll':d_o_l_coll,
    'm_s_coll':m_s_coll,'o_f_coll':o_f_coll,'no_of_pro':no_of_pro,'project_title':pro_title,'project_desc':pro_description,'project_mem':pro_members,      'project_pub':pro_publications,'project_from':pro_from,'project_to':pro_to,'project_link':pro_links,'name_company':name_company,'place_company':place_company,
    'from_company':from_company,'to_company':to_company,'pos_company':pos_company,'no_of_emp':no_of_emp,'no_of_skill':no_of_skill,'name_skill':name_skill,"level_skill":level_skill}
