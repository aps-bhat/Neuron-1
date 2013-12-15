class ProfilePicture(object):
  def __init__(self,request):
     self.settings = request.registry.settings
     self.collection = request.db['profile_pictures'] # to store the details of the user for the current picture

  def EnterFirstProfPic(self,request,username,photo_description):
     latest=0
     last_up=0
     pic_det={'username':username, 'current_picture_id':latest , 'last_id':last_up }
     self.collection.insert(pic_det)
     table_name=username+'_profile_picture'
     self.collection = request.db[table_name]
     upic_det={'photo_id':latest,'photo_description':photo_description}
     self.collection.insert(upic_det)
