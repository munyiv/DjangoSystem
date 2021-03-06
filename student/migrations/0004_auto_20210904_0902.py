# Generated by Django 3.2.5 on 2021-09-04 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_alter_student_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('Female', 'Female'), ('Male', 'Male'), ('Other', 'Other')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='languages',
            field=models.CharField(choices=[('English', 'English'), ('Swahili', 'Swahili'), ('French', 'French'), ('Kinyarwanda', 'Kinyaruanda')], max_length=15, null=True),
        ),
    ]
