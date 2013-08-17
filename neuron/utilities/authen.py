class Authen(object):
  def __init__(self,request):
     self.settings = request.registry.settings
     self.collection = request.db['users']
  
  def CheckUser(self,uname,pword):
     UserEntry=self.collection.find_one({'username':uname})
     if UserEntry:
        PassEntry=UserEntry['password']
        if(PassEntry == pword): 
            return True
        else:
            return False
     else:
        return False
     


