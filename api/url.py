from django.conf.urls import url
from django.contrib import admin
from miniProject import views
from api import views


urlpatterns = [
    # url(r'^hello/', views.hello),
    # url(r'^world/', views.runoob),
    url(r'^login/', views.LoginView.as_view()),
]