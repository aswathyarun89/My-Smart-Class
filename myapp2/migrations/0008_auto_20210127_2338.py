# Generated by Django 3.1.2 on 2021-01-27 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp2', '0007_auto_20201223_0909'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course_info',
            name='id',
        ),
        migrations.AlterField(
            model_name='course_info',
            name='Course_Descrp',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='course_info',
            name='Course_Duration',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='course_info',
            name='Course_EndDate',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='course_info',
            name='Course_Id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='course_info',
            name='Course_Logo',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='course_info',
            name='Course_StartDate',
            field=models.DateField(blank=True),
        ),
    ]
