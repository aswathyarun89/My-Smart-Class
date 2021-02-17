# Generated by Django 3.1.2 on 2021-01-27 23:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp2', '0011_delete_course_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course_Info',
            fields=[
                ('Course_Id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('Course_Name', models.CharField(max_length=30)),
                ('Course_Descrp', models.CharField(blank=True, max_length=200)),
                ('Course_Duration', models.CharField(blank=True, max_length=20)),
                ('Course_Logo', models.CharField(blank=True, max_length=50)),
                ('Course_StartDate', models.DateField(blank=True)),
                ('Course_EndDate', models.DateField(blank=True)),
                ('Course_Owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp2.user_info')),
            ],
        ),
    ]
