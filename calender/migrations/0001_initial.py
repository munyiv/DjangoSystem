# Generated by Django 3.2.5 on 2021-08-15 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=12, null=True)),
                ('last_name', models.CharField(max_length=12, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('national_id', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]
