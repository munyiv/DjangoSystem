from django.urls import include,path
from rest_framework import routers
from .views import CoursesViewSet, StudentViewSet, TrainerViewSet,CalenderViewSet

router = routers.DefaultRouter()
router.register(r"student", StudentViewSet)
router.register(r"trainer",TrainerViewSet)
router.register(r"calender",CalenderViewSet)
router.register(r"courses",CoursesViewSet)



urlpatterns=[
    path("", include(router.urls))

]