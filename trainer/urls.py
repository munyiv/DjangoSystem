from django.conf.urls import url
from django.urls import path
# from django.urls.resolvers import URLPattern
from .views import edit_trainer, register_trainer, trainer_profile,trainers_list

urlpatterns=[
    path("register",register_trainer,name="register_trainer"),
    path("list/",trainers_list,name="trainers_list"),
    path("profile/<int:id>/",trainer_profile,name="trainer_profile"),
    path("edit/<int:id>/",edit_trainer,name="edit_trainer"),
]