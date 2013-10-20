class RegisterUser(object):
  def __init__(self,request):
     self.settings = request.registry.settings
     self.collection = request.db['users']

  def EnterUser(self, username, password, email,fname,lname):
     user={'username':username, 'password':password, 'email_id':email,'first_name':fname,'last_name':lname}
     self.collection.insert(user)
