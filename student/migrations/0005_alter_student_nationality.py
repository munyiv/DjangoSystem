# Generated by Django 3.2.5 on 2021-10-04 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_auto_20210904_0902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='nationality',
            field=models.CharField(choices=[('Kenyan', 'Kenyan'), ('Rwandan', 'Rwandan'), ('S.Sudanese', 'SouthSudanese'), ('Ugandan', 'Ugandan')], max_length=15, null=True),
        ),
    ]
