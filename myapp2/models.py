from django.db import models

# Create your models here.

class User_Info(models.Model):
    User_Reg_No=models.BigIntegerField(primary_key = True)
    User_Reg_Date=models.DateField()
    User_Joining_Date=models.DateField()
    First_Name=models.CharField(max_length=30)
    Last_Name=models.CharField(max_length=30)
    Full_Name=models.CharField(max_length=50,blank=True)
    Date_Birth=models.DateField(blank=True)
    Mobile_No=models.BigIntegerField()    
    Address=models.CharField(max_length=50)
    Email=models.CharField(max_length=20)   
    Status=models.CharField(max_length=10)
    User_Photo=models.CharField(max_length=50,blank=True)
    Gender=models.CharField(max_length=6)

class User_Cred(models.Model):
    User_Type=models.CharField(max_length=10)
    User_Id=models.CharField(max_length=30)
    Password=models.CharField(max_length=20)
    User_Reg_No=models.ForeignKey(User_Info,on_delete=models.CASCADE)

class Course_Info(models.Model):
    Course_Id=models.BigIntegerField(primary_key = True)
    Course_Name=models.CharField(max_length=30)
    Course_Descrp=models.CharField(max_length=200,blank=True)
    Course_Duration=models.CharField(max_length=20,blank=True)
    Course_Logo=models.CharField(max_length=50,blank=True)
    Course_StartDate=models.DateField(blank=True)
    Course_EndDate=models.DateField(blank=True)
    Course_Owner=models.CharField(max_length=30)
    Course_Owner_Id=models.ForeignKey(User_Info,on_delete=models.CASCADE)

class Course_Student_Map(models.Model):
    CSM_Id=models.BigIntegerField(primary_key = True)
    Course_Id=models.ForeignKey(Course_Info,on_delete=models.CASCADE)
    User_Reg_No=models.ForeignKey(User_Info,on_delete=models.CASCADE)
    Assigned_Date=models.DateField(blank=True)
    CSM_Status=models.CharField(max_length=20,blank=True)
    Course_Progress=models.BigIntegerField()
    







