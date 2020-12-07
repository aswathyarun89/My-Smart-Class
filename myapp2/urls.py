from django.urls import path
from . import views
urlpatterns = [
    # Admin Module Path
    path('',views.myfunction,name="pgm"),
    path('admindashboard/',views.dashboard,name="admindashboard"),
    # path('addins',views.addinstructor,name="addins"),
    # path('addstu',views.addstudent,name="addstu"),
    # path('createcourse',views.createcourse,name="createcourse"),
    # path('inscal',views.instructorcalendar,name="inscal"),
    # path('admindashboard', views.dashboard1, name='admindashboard'),
    
    

    # Instructor Module Path
    # path('addstuins',views.addstudentinspage,name="addstuins"),
    # path('createcourseins',views.createcourseinspage,name="createcourseins"),
    # path('inscalins',views.instructorcalendarinspage,name="inscalins"),
    # path('viewassigncourse',views.assignedcoursesins,name="viewassigncourse"),
    # path('scheclass',views.scheduleclass,name="scheclass"),
    # path('insdashboard', views.instructordashboard, name='insdashboard'),

    # Student Module Path
    # path('studashboard',views.studentdashboard,name="studashboard"),
    # path('stucourse',views.viewstudentcourse,name="stucourse"),
    # path('stuassignments',views.studentassignment,name="stuassignments"),
    # path('stuassessments',views.studentassessment,name="stuassessments"),
    # path('stucertificate',views.studentcertificate,name="stucertificate"),
        

]