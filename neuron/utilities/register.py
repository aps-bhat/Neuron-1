class RegisterUser(object):
  def __init__(self,request):
     self.settings = request.registry.settings
     self.collection = request.db['users']

  def EnterUser(self, username, password, email):
     user={'username':username, 'password':password, 'email_id':email }
     self.collection.insert(user)
