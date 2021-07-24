from django.db import models

# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=12)
    last_name=models.CharField(max_length=12)
    age=models.PositiveSmallIntegerField()
    date_of_birth=models.DateField()
    national_id=models.CharField(max_length=20)
    # nationality=models.ListField()
    # gender=models.ChoiceField("male")
    guardian_name=models.CharField(max_length=12)
    email_adress=models.EmailField()
    county=models.CharField(max_length=15)
    # phone_number=models.PhoneNumberField()
    medical_report=models.FileField()
    # languages=models.ListField()
    date_of_enrollement=models.DateField()
    course_name=models.CharField(max_length=12)
    laptop_number=models.CharField(max_length=10)
    # profile=models.ImageField()


    