from django.db import models

# Create your models here.
class Courses(models.Model):
    course_name=models.CharField(max_length=20,null=True)
    course_code=models.CharField(max_length=20,null=True)
    course_schedule=models.FileField(upload_to="documents/",blank=True)
    syllabus=models.TextField(blank=True)
    course_duration=models.CharField(max_length=20,null=True)
    course_trainer=models.CharField(max_length=18,null=True)
    course_time=models.DurationField(null=True)
    image=models.ImageField(upload_to ="images/",null=True)

    

    