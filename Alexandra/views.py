from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseServerError
from django.core import serializers
from django import forms
from django.template import RequestContext
from .models import Post
from .models import PostForm
from .models import User_post
from .models import Comments
from django.views.decorators.csrf import csrf_exempt
from django.contrib.sessions.models import Session
from django.contrib.auth.decorators import login_required 
#from django.core.cache import cache
#import cPickle as pickle
from registration.forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
import redis
import json
# from .models import Document
# from .forms import DocumentForm
def index(request):
#    user = User.objects.all()
    #names = ",".join(map(lamda x:x.username, user))
#    data = serializers.serialize('json', user)
#    return HttpResponse(data)
    return HttpResponse('test')

def posts(request):
    latest_posts = Post.objects.order_by('-created_at')[:10]
#    user_posts = map(lambda x:{'text_content':x.text_content,
#                                  'image':x.image,
#                                  'id':x.id,
#                                  'username':User.objects.get(
#                                      id=(User_post.objects.get(post=x.id).user)).username},
#                            latest_posts)
    
#    comments = Comments.objects.order_by('-created_at')[:10:-1]
#    comments = reversed(comments)
    context = {#'latest_posts':latest_posts,
                'form':PostForm(),
#                'comments': comments, 
                'user':request.user,
                'r_form':RegistrationForm,
                'l_form':AuthenticationForm}

    return render(request, 'Alexandra/index.html', context)


def post(request, post_id):
    if not Post.objects.filter(id=post_id):
        return HttpResponse('Bad post id')
    thispost = Post.objects.get(id=post_id)
    return render(request, 'Alexandra/single_post.html', {'post': thispost})


def new_post(request):
    if not request.user.is_authenticated():
        return redirect('../accounts/login')
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            user_post = User_post(post = form.save(commit=True), user = request.user)
            user_post.save()
            return redirect('../')
        else:
            print form.errors
    else:
         form = PostForm()
    return redirect('../')

 
@csrf_exempt
def node_api(request):
    try:
        #Get User from sessionid
        #session = Session.objects.get(session_key=request.POST.get('sessionid'))
        #user_id = session.get_decoded().get('_auth_user_id')
        #user = User.objects.get(id=user_id)
 
        #Create comment
        username = request.POST.get("username")
        comment = request.POST.get("comment")
        print(request.POST.get("id"))
        print(username)
        print(comment)
        Comments.objects.create(text=username + ": " + comment)
        
        #Once comment has been created post it to the chat channel
        r = redis.StrictRedis(host='localhost', port=6379, db=0)
        r.publish('chat', username + ': ' + comment)

        return HttpResponse("Everything worked :)")
    except Exception, e:
        return HttpResponseServerError(str(e))


#def set_cache(request):
#
#    latest_view = Post.objects.order_by('-created_at')[:10]
#    context = {'latest_posts' : latest_view, 'form':PostForm()}
#
#    in_cache = cache.get('latest_view')
#
#    if in_cache:
#      return render(request, 'Alexandra/index.html', in_cache)
#    else:
#      cache.set('latest_view', cPickle.dump(context, 60*15))
#
#    return HttpResponse(message)
