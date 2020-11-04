from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', auth_views.LoginView.as_view(), {'template_name': 'main/login.html'}, name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
]
