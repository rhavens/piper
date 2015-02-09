from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import User
from .models import Post

#def index(request):
#  user = User.objects.all()
#  #names = ",".join(map(lamda x:x.username, user))
#  data = serializers.serialize('json', user)
#  return HttpResponse(data)


def posts(request):
  latest_posts = Post.objects.order_by(id)
  context = {'latest_posts' : latest_posts}
  return render(request,'Alexandra/index.html',  context)
  

# Create your views here.
