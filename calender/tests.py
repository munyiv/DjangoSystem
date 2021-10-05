from django.test import TestCase
from .models import Calender
from django .urls import reverse




class CalenderModelsTestCase(TestCase):
    def setUp(self):
        self.calender= Calender(
        venue= "nakuru",
        event_id="28098",
        event_name= "Kalasha Festival",
        event_planner="Audrey Munyiva"
        )
    
    def test_register_calender_view(self):  
        url=reverse('register_calender')
        data={
            "venue":self.calender.venue,
            "event_id":self.calender.event_id,
            "event_name":self.calender.event_name,
            "event_planner":self.calender.event_planner
            }
        request=self.client.post(url,data)
        self.assertEqual(request.status_code,200)

    
    def test_calender_list_view(self):
        url=reverse('calender_list')
        data={
            "venue":self.calender.venue,
            "event_id":self.calender.event_id,
            "event_name":self.calender.event_name,
            "event_planner":self.calender.event_planner,

            }
        request=self.client.post(url,data)
        self.assertEqual(request.status_code,200)
    
   



# Create your tests here.
