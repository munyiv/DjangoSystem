from django.conf.urls import url
from django.urls import path
# from django.urls.resolvers import URLPattern
from .views import home
# from.import views
urlpatterns=[
    path("", home ,name="home_view"),
    

]