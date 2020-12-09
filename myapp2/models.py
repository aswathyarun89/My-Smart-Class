from django.db import models

# Create your models here.

class User_info(models.Model):
    User_reg_no=models.BigIntegerField()
    User_reg_Date=models.DateField()
    User_joining_Date=models.DateField()
    First_Name=models.CharField(max_length=30)
    Last_Name=models.CharField(max_length=30)
    Date_Birth=models.DateField()
    Mobile_no:models.BigIntegerField()
    Address=models.CharField(max_length=50)
    User_Photo=models.CharField(max_length=50)


