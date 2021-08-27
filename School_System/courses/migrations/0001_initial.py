# Generated by Django 3.2.5 on 2021-08-15 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=12, null=True)),
                ('last_name', models.CharField(max_length=12, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('national_id', models.CharField(max_length=20, null=True)),
                ('nationality', models.CharField(choices=[('1', 'Kenyan'), ('2', 'Rwandan'), ('3', 'SouthSudanese'), ('4', 'Ugandan')], max_length=15, null=True)),
                ('gender', models.CharField(choices=[('1', 'Female'), ('2', 'Male'), ('3', 'Other')], max_length=15, null=True)),
                ('guardian_name', models.CharField(max_length=12, null=True)),
                ('email_adress', models.EmailField(max_length=254, null=True)),
                ('county', models.CharField(max_length=15, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('languages', models.CharField(choices=[('1', 'English'), ('2', 'Swahili'), ('3', 'French'), ('4', 'Kinyarwanda')], max_length=15, null=True)),
                ('date_of_enrollement', models.DateField(null=True)),
                ('course_name', models.CharField(blank=True, max_length=12, null=True)),
                ('laptop_number', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
    ]