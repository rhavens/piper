from django.db import models
from django.forms import ModelForm, Textarea, URLInput
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin import widgets
import datetime
from django.utils import timezone


#class User(models.Model):
#    id = models.AutoField(primary_key=True)
#    username = models.CharField(max_length = 60)
#    password = models.CharField(max_length = 60)
#    email = models.CharField(max_length = 254)
#    birthday = models.IntegerField(8)
#    MALE = "M"
#    FEMALE = "F"
#    OTHER = "O"
#    GENDER_REGISTRATION = (
#      (MALE, 'Male'),
#      (FEMALE, 'Female'),
#      (OTHER, 'Other'),
#    )
#    gender = models.CharField(max_length = 1, choices = GENDER_REGISTRATION, default = OTHER)
    

class Post (models.Model):
    id = models.AutoField(primary_key=True)
    text_content = models.CharField(max_length = 200)
# for the mvp, perhaps just store a link instead of an s3 key
    image_key = models.CharField (max_length = 1024)
    created_at = models.DateTimeField(editable=False, default=timezone.now)
    last_modified = models.DateTimeField(default=timezone.now)
    def save(self, *args, **kwargs):
        if not self.id:
            self.created = datetime.datetime.today()
        self.modified = datetime.datetime.today()
        return super(Post, self).save(*args, **kwargs)
    class Meta:
        get_latest_by = 'last_modified'
        ordering = ['-last_modified']

class PostForm (ModelForm):
    class Meta:
        model = Post
        fields = ['image_key', 'text_content']
        labels = {
            'text_content': _('Description'),
            'image_key': _('Image'),
        }
        error_messages = {
            'text_content': {
                'max_length': _('Character limit is 200 characters'),
            },
        }
        widgets = {
            'text_content': Textarea(attrs={'cols': 50, 'rows': 5}),
            'image_key': URLInput(),
        }

#class Comment (models.Model):
#    id = models.AutoField(primary_key=True)
#    username = models.CharField(max_length = 60)
#    content = models.CharField(max_length = 1024)
#    timestamp = models.DateTimeField('Posted: ')
    
#class User_post(models.Model):
#    user = models.ForeignKey(User)
#    post = models.ForeignKey(Post)
    
#class Posts_comments (models.Model):
#    post = models.ForeignKey(Post)
#    comment = models.ForeignKey(Comment)
    
  
