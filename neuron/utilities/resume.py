class Resume(object):
  def __init__(self,request):
     self.settings = request.registry.settings
     self.collection = request.db['resume']
     self.collection_school=request.db['school']

  def resumeread(self,uname):
    res=self.collection.find_one({'username':uname})
    print res
    #check_address=Resume.get('address',None)
    try:
        Address=res['address']
    except TypeError:
        Address='Enter your address'
    schools=[]
    name=[]
    d_o_j=[]
    d_o_l=[]
    place=[]
    m_s=[]
    o_f=[]
    no_of_p=0
    try:
        schools=res['school']
    except TypeError:
        schools=[]
    i=0
    for school in schools:
        school_detail=self.collection_school.find_one({'sid':school})
        name.append(school_detail['name'])
        d_o_j.append(school_detail['date_of_joining'])
        d_o_l.append(school_detail['date_of_leaving'])
        place.append(school_detail['place'])
        m_s.append(school_detail['marks_secured'])
        o_f.append(school_detail['out_of'])
        i=i+1
    no_of_p=i;
    print "at the end"
    print Address,uname,no_of_p,name,d_o_j,d_o_l,place,m_s,o_f
    return {'address':Address,'username':uname,'no_of_p':no_of_p,'name':name,'d_o_j':d_o_j,'d_o_l':d_o_l,'place':place,'m_s':m_s,'o_f':o_f}
