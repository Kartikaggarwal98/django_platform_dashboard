from django.conf.urls import patterns, include, url
from django.contrib import admin
from oauth.views import *
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'social_auth.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/',index,name="social_auth"),
)
