# Generated by Django 3.1.2 on 2020-12-21 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='user1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
    ]
