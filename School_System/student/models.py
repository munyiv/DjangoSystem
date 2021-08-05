from django.db import models

# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=12)
    last_name=models.CharField(max_length=12)
    age=models.PositiveSmallIntegerField()
    date_of_birth=models.DateField()
    national_id=models.CharField(max_length=20)
    nationality=(
        ('1','Kenyan'),
        ('2','Rwandan'),
        ('3','SouthSudanese'),
        ('4','Ugandan'),
    )
    nationality=models.CharField(
        max_length=15 , choices=nationality
    )
    gender=(
        ('1','Girl'),
        ('2','Boy'),
        ('3','Other'),
    )
    gender=models.CharField(max_length=15,choices=gender)
    guardian_name=models.CharField(max_length=12)
    email_adress=models.EmailField()
    county=models.CharField(max_length=15)
    image=models.ImageField(upload_to ="images/")
    # phone_number=models.PhoneNumberField()
    medical_report=models.FileField(upload_to="documents/")
    languages=(
        ('1','English'),
        ('2','Swahili'),
        ('3','French'),
        ('4','Kinyaruanda'),
    )
    languages=models.CharField(max_length=15,choices=languages)
    date_of_enrollement=models.DateField()
    course_name=models.CharField(max_length=12)
    laptop_number=models.CharField(max_length=10)



    