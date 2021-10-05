from django.db import models
import datetime

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
        ('Female','Female'),
        ('male','Male'),
        ('Other','Other'),
    )
    gender=models.CharField(max_length=15,choices=gender)
    email_adress=models.EmailField(null=True)
    county=models.CharField(max_length=15,null=True)
    image=models.ImageField(upload_to ="images/",null=True)
    bio=models.TextField(null=True)
    contract=models.FileField(upload_to="documents/",null=True)
    date_hired=models.DateField(null=True)
    languages=(
        ('English','English'),
        ('Swahili','Swahili'),
        ('French','French'),
        ('Kinyarwanda','Kinyaruanda'),
    )
    languages=models.CharField(max_length=15,choices=languages,null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def year_of_birth(self):
        current_year=datetime.datetime.now().year
        year= current_year
        return year -self.age
    
    
