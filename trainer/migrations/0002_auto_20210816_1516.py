# Generated by Django 3.2.5 on 2021-08-16 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainer',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='trainer',
            name='medical_report',
        ),
        migrations.AddField(
            model_name='trainer',
            name='age',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='trainer',
            name='bio',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='trainer',
            name='contract',
            field=models.FileField(null=True, upload_to='documents/'),
        ),
        migrations.AddField(
            model_name='trainer',
            name='date_hired',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]