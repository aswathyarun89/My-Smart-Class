# Generated by Django 3.1.2 on 2020-12-21 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp2', '0002_user1'),
    ]

    operations = [
        migrations.DeleteModel(
            name='user',
        ),
        migrations.DeleteModel(
            name='user1',
        ),
    ]