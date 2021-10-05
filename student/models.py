from django.db import models

# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=12, null=True)
    last_name=models.CharField(max_length=12, null=True)
    age=models.PositiveSmallIntegerField(null=True)
    date_of_birth=models.DateField(blank=True,null=True)
    national_id=models.CharField(max_length=20,null=True)
    nationality=(
        ('Kenyan','Kenyan'),
        ('Rwandan','Rwandan'),
        ('S.Sudanese','SouthSudanese'),
        ('Ugandan','Ugandan'),
    )
    nationality=models.CharField(
        max_length=15 , choices=nationality
    ,null=True)
    gender=(
        ('Female','Female'),
        ('Male','Male'),
        ('Other','Other'),
    )
    gender=models.CharField(max_length=15,choices=gender, null=True)
    guardian_name=models.CharField(max_length=12,null=True)
    email_adress=models.EmailField(null=True)
    county=models.CharField(max_length=15,null=True)
    image=models.ImageField(upload_to ="images/",null=True)
    languages=(
        ('English','English'),
        ('Swahili','Swahili'),
        ('French','French'),
        ('Kinyarwanda','Kinyaruanda'),
    )
    languages=models.CharField(max_length=15,choices=languages,null=True)
    date_of_enrollement=models.DateField(null=True)
    course_name=models.CharField(max_length=12,blank=True,null=True)
    laptop_number=models.CharField(max_length=10,blank=True,null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    
  



    