from django.conf.urls import url
from django.test import TestCase
from .models import Student
from django.urls import reverse 
from django.test import Client





class StudentModelsTestCase(TestCase):
    def setUp(self):
        self.student=Student(first_name= "Munyivs",
        last_name="Elizabeth",
        age= 20,
        gender= "female",
        email_adress="munyivs@gmail.com",
        county="Nakuru",
        national_id="849020"
        )
    def test_full_name_contains_first_name(self):
        self.assertIn(self.student.first_name,self.student.full_name())

    def test_full_name_contains_last_name(self):
        self.assertIn(self.student.last_name,self.student.full_name())
    
    def test_register_student_view(self):  
        url=reverse('register_student')
        data={
            "first_name":self.student.first_name,
            "last_name":self.student.last_name,
            "age":self.student.age,
            }
        request=self.client.post(url,data)
        self.assertEqual(request.status_code,200)

    def test_student_list_view(self):
        url=reverse('student_list')
        data={
            "first_name":self.student.first_name,
            "last_name":self.student.last_name,
            "age":self.student.age,
            }
        request=self.client.post(url,data)
        self.assertEqual(request.status_code,200)

# Create your tests here.
