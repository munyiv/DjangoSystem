from django.conf.urls import url
from django.urls import path
# from django.urls.resolvers import URLPattern
from .views import register_calender,calendar_list,calender_profile,edit_calender
from.import views
urlpatterns=[
    path("register",register_calender,name="register_calender"),
    path("list/",calendar_list,name="calender_list"),
    path("calender/",views.CalendarView.as_view(),name="calendar"),
    path("profile/<int:id>/",calender_profile,name="calendar_profile"),
    path("edit/<int:id>/",edit_calender,name="edit_calendar"),

]