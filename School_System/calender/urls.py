from django.conf.urls import url
from django.urls import path
# from django.urls.resolvers import URLPattern
from .views import register_student,calendar_list
from.import views
urlpatterns=[
    path("register",register_student,name="register_student"),
    path("list/",calendar_list,name="student_list"),
    path("calender/",views.CalendarView.as_view(),name="calendar"),

]