from django.contrib import admin
from .models import Post, User
#from .models import User, Post, Comment, User_post, Posts_comments 
admin.site.register(User)
admin.site.register(Post)
#admin.site.register(Comment)
#admin.site.register(User_post)
#admin.site.register(Posts_comments)
# Register your models here.
