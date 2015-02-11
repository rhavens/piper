from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django import forms
from django.template import RequestContext
#from .models import User
from .models import Post
from .models import PostForm

def index(request):
#    user = User.objects.all()
    #names = ",".join(map(lamda x:x.username, user))
#    data = serializers.serialize('json', user)
#    return HttpResponse(data)
    return HttpResponse('test')


def posts(request):
    latest_posts = Post.objects.all()
    context = {'latest_posts' : latest_posts}
    return render(request, 'Alexandra/index.html', context)

def post(request, post_id):
    thispost = Post.objects.get(id=post_id)
    return render(request, 'Alexandra/single_post.html', {'post': thispost})

def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return posts(request)
        else:
            print form.errors
    else:
         form = PostForm()
    return render(request, 'Alexandra/new_post.html', {'form': form})
    

# Create your views here.
