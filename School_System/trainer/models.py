from django.db import models

# Create your models here.
class Trainer(models.Model):
    first_name=models.CharField(max_length=12, null=True)
    last_name=models.CharField(max_length=12, null=True)
    age=models.PositiveSmallIntegerField(null=True)
    national_id=models.CharField(max_length=20,null=True)
    nationality=(
        ('1','Kenyan'),
        ('2','Rwandan'),
        ('3','SouthSudanese'),
        ('4','Ugandan'),
    )
    nationality=models.CharField(
        max_length=15 , choices=nationality
    ,null=True)
    gender=(
        ('1','Female'),
        ('2','Male'),
        ('3','Other'),
    )
    gender=models.CharField(max_length=15,choices=gender)
    email_adress=models.EmailField(null=True)
    county=models.CharField(max_length=15,null=True)
    image=models.ImageField(upload_to ="images/",null=True)
    bio=models.TextField(null=True)
    contract=models.FileField(upload_to="documents/",null=True)
    date_hired=models.DateField(null=True)
    languages=(
        ('1','English'),
        ('2','Swahili'),
        ('3','French'),
        ('4','Kinyaruanda'),
    )
    languages=models.CharField(max_length=15,choices=languages,null=True)
