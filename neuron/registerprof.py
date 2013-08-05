class RegisterProfile(object):
  def __init__(self,request):
     self.settings = request.registry.settings
     self.collection = request.db['profile']

  def EnterProfDetails(self, username, fname, lname, date, month, year, city, designation):
     profile={'username':username, 'fname':fname, 'email_id':email } #to be changed
     self.collection.insert(user)
