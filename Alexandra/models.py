from django.db import models

# Create your models here.

from django.db import models

class User(models.Model):
  id = models.AutoField(primary_key=True)
  username = models.CharField(max_length = 60)
  password = models.CharField(max_length = 60)
  email = models.CharField(max_length = 254)
  birthday = models.IntegerField(8)
  MALE = "M"
  FEMALE = "F"
  OTHER = "O"
  GENDER_REGISTRATION = (
    (MALE, 'Male'),
    (FEMALE, 'Female'),
    (OTHER, 'Other'),
  )
  gender = models.CharField(max_length = 1, choices = GENDER_REGISTRATION, default = OTHER)
  
class Post (models.Model):
  id = models.AutoField(primary_key=True)
  text_content = models.CharField(max_length = 200)
  image_key = models.CharField (max_length = 1024)
  timestamp = models.DateTimeField('Posted: ')
  
class Comment (models.Model):
  id = models.AutoField(primary_key=True)
  username = models.CharField(max_length = 60)
  content = models.CharField(max_length = 1024)
  timestamp = models.DateTimeField('Posted: ')
  
class User_post(models.Model):
  user = models.ForeignKey(User)
  post = models.ForeignKey(Post)
  
class Posts_comments (models.Model):
  post = models.ForeignKey(Post)
  comment = models.ForeignKey(Comment)
  
 