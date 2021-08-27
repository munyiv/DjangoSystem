from django.conf.urls import url
from django.urls import path
# from django.urls.resolvers import URLPattern
from .views import register_student,trainers_list
urlpatterns=[
    path("register",register_student,name="TrainersForm"),
    path("list/",trainers_list,name="trainers_list"),
]