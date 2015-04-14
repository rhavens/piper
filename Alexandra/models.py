from django.db import models
from django.forms import ModelForm, Textarea, FileInput
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin import widgets
import datetime
from django.utils import timezone



class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)
    email = models.CharField(max_length = 254)
#    birthday = models.IntegerField(8)
    GENDER_REGISTRATION = (
      ('M', 'Male'),
      ('F', 'Female'),
      ('O', 'Other'),
    )
    gender = models.CharField(max_length = 1, choices = GENDER_REGISTRATION, default = 'O')
    created_at = models.DateTimeField(editable=False, default=timezone.now)
    last_modified = models.DateTimeField(default=timezone.now)
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = datetime.datetime.today()
        self.last_modified = datetime.datetime.today()
        return super(User, self).save(*args, **kwargs)

   

class Post (models.Model):
    id = models.AutoField(primary_key=True)
    text_content = models.CharField(max_length = 200)
# for the mvp, perhaps just store a link instead of an s3 key
    image = models.ImageField(upload_to='Alexandra', default='NULL')
    created_at = models.DateTimeField(editable=False, default=timezone.now)
    last_modified = models.DateTimeField(default=timezone.now)
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = datetime.datetime.today()
        self.last_modified = datetime.datetime.today()
        return super(Post, self).save(*args, **kwargs)
    class Meta:
        get_latest_by = 'last_modified'
        ordering = ['-last_modified']

class PostForm (ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'text_content']
        labels = {
            'text_content': _('Description'),
            'image': _('Image'),
        }
        error_messages = {
            'text_content': {
                'max_length': _('Character limit is 200 characters'),
            },
        }
        widgets = {
            'text_content': Textarea(attrs={'cols': 50, 'rows': 5}),
            'image': FileInput(),
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
    
  
