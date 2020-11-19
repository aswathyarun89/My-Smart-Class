from django.urls import path
from . import views
urlpatterns = [
    path('',views.myfunction,name="pgm"),
    path('admindashboard',views.dashboard,name="admindashboard"),
    path('addins',views.addinstructor,name="addins"),
    path('addstu',views.addstudent,name="addstu"),
    path('createcourse',views.createcourse,name="createcourse"),
    path('inscal',views.instructorcalendar,name="inscal"),
    path('admindashboard', views.dashboard1, name='admindashboard'),
        

]