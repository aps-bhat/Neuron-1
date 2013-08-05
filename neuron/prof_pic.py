class ProfilePicture(object):
  def __init__(self,request):
     self.settings = request.registry.settings
     self.collection = request.db['prof_pic']

  def EnterFirstProfPic(self, username):
     latest=0
     last_up=0
     pic_det={'username':username, 'last_used':latest , 'last_uploaded':last_up }
     self.collection.insert(pic_det)
