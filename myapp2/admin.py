from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(User_Info)
admin.site.register(User_Cred)
admin.site.register(Course_Info)






