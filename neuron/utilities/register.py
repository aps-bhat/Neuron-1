class RegisterUser(object):
  def __init__(self,request):
     self.settings = request.registry.settings
     self.collection = request.db['users']

  def EnterUser(self, username, password, email):
     user={'username':username, 'password':password, 'email_id':email}
     self.collection.insert(user)
  
  def EnterUserDetails(self,username,fname,lname,date,month,year,city,desg):
	 details={'first_name':fname,'last_name':lname,'d_o_b':date,'m_o_b':month,'y_o_b':year,'c_city':city,'c_des':desg}
	 self.collection.update({'username':username},{"$set":details},upsert=True)
	
