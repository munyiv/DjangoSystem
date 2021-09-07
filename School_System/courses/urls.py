from django.urls import path
from .views import register_student,courses_list,courses_profile,edit_courses
urlpatterns=[
    path("register",register_student,name="courses"),
    path("list/",courses_list,name="courses_list"),
    path("profile/<int:id>/",courses_profile,name="courses_profile"),
    path("edit/<int:id>/",edit_courses,name="edit_course"),
]