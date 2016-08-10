from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
 #url('^', include('django.contrib.auth.urls')),
  url(r'^$', views.index, name = 'index'),
  url('^login/$', auth_views.login, { 'template_name': 'swift/registration/login.html'}),
  url('^logout/$', auth_views.logout, { 'template_name': 'swift/registration/logged_out.html'}),
]
