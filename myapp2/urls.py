from django.urls import path
from . import views
urlpatterns = [
    # Admin Module Path
    path('',views.myfunction,name="pgm"),
    path('admindashboard/',views.dashboard,name="admindashboard"),
    path('addins/',views.addinstructor,name="addins"),
    path('addstu/',views.addstudent,name="addstu"),
    path('createcourse/',views.createcourse,name="createcourse"),
    path('inscal',views.instructorcalendar,name="inscal"),
    path('insformsubmit',views.addinstructorform,name="insformsubmit"),
    path('addcourse',views.addcourseform,name="addcourse"),
    path('loginform',views.loginfun,name='loginform'),
    path('logout',views.logoutfun,name="logout"),
    # Check if the username already exists
    path('addins/inputcheck',views.inputcheckfun,name="inputcheck"),
    path('addins/exact_url/',views.your_view,name="exact_url"),
    path('addins/exact_url/view_data_aj',views.viewdataajfun,name="view_data_aj"),
    path('addins/exact_url/update_aj',views.update_ajfun,name="update_aj"),
    
    
    
  
    
    

    # Instructor Module Path
    path('insdashboard/', views.instructordashboard, name='insdashboard'),
    path('addstuins/',views.addstudentinspage,name="addstuins"),
    path('createcourseins/',views.createcourseinspage,name="createcourseins"),
    path('inscalins/',views.instructorcalendarinspage,name="inscalins"),
    path('viewassigncourse/',views.assignedcoursesins,name="viewassigncourse"),
    path('scheclass/',views.scheduleclass,name="scheclass"),
    path('asgmt/',views.assignments,name="asgmt"),
    path('assesmt/',views.assessments,name="assesmt"),
    path('document/',views.documents,name="document"),
    path('cert/',views.certificate,name="cert"),
    

    # Student Module Path
    path('studashboard/',views.studentdashboard,name="studashboard"),
    path('stucourse/',views.viewstudentcourse,name="stucourse"),
    path('stuassignments/',views.studentassignment,name="stuassignments"),
    path('stuassessments/',views.studentassessment,name="stuassessments"),
    path('stucertificate/',views.studentcertificate,name="stucertificate"),
        
# Login Function


]