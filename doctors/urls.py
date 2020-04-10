from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^login/$', views.login, name="login"),
    url(r'^login_page/$', views.login_page, name="login_page"),
    url(r'^signup/$', views.signup, name="signup"),
    url(r'^createaccount/$', views.create_account, name="signup"),
]