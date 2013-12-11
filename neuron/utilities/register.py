class RegisterUser(object):
  def __init__(self,request):
     self.settings = request.registry.settings
     self.collection = request.db['users']

  def EnterUser(self, request, username, password, email):
     flag=self.collection.find_one({'username':username})
     if not flag:	
     	user={'username':username, 'password':password, 'email_id':email,'social_domain':'direct'}
     	self.collection.insert(user)
     else: 
		#print "hi"
		return 1
     return 0	
		#redirect('0.0.0.0:5000/')
		#HTTPFound(location='http://0.0.0.0:5000')
  
  def EnterUserDetails(self,username,fname,lname,date,month,year,city,desg):
	 details={'first_name':fname,'last_name':lname,'d_o_b':date,'m_o_b':month,'y_o_b':year,'c_city':city,'c_des':desg}
	 self.collection.update({'username':username},{"$set":details},upsert=True)
	
