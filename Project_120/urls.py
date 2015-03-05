from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Project_120.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('Alexandra.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
