from django.conf.urls import url
from django.test import TestCase
from .models import Courses
from django.urls import reverse 




class CoursesModelsTestCase(TestCase):
    def setUp(self):
        self.course=Courses(
        course_name= "Python",
        course_code="28098",
        course_trainer= "Mwai",
        
        )
    def test_register_course_view(self):  
        url=reverse('register_course')
        data={
            "course_code":self.course.course_code,
            "course_name":self.course.course_name,
            "course_trainer":self.course.course_trainer,
            }
        request=self.client.post(url,data)
        self.assertEqual(request.status_code,200)
    
    def test_courses_list_view(self):
        url=reverse('courses_list')
        data={
            "course_code":self.course.course_code,
            "course_name":self.course.course_name,
            "course_trainer":self.course.course_trainer,
            }
        request=self.client.post(url,data)
        self.assertEqual(request.status_code,200)
        
        
        
        # Create your tests here.
