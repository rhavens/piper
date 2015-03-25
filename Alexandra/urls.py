from django.conf.urls import patterns , include,  url
from django.conf import settings
from django.conf.urls.static import static
from Alexandra import views
from Alexandra.api import PostResource, UserResource

post_resource = PostResource()
user_resource = UserResource()

urlpatterns = patterns ( '',
#    url(r'^$', views.posts, name = 'index' ),
    url(r'^$', views.posts, name = 'posts'),
    url(r'^post/(?P<post_id>\d+)', views.post, name = 'post'),
    url(r'^new_post/', views.new_post, name = 'new_post'),
    url(r'^api/posts/', include(post_resource.urls)),
    url(r'^api/users/', include(user_resource.urls)),
    )

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
