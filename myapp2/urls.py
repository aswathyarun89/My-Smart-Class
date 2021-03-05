from django.urls import path
from . import views
urlpatterns = [
# Admin Module Path
    path('',views.myfunction,name="pgm"),
    path('admindashboard/',views.dashboard,name="admindashboard"),

# Add/Update Instructor html page begins

# Add/Update Instructor html page with displaying the page except the Userdetails
    path('addins/',views.addinstructor,name="addins"),

# Add/Update Instructor html page with displaying the page with userdetails
    path('addins/dis_data_addins',views.displaydataajfun,name="dis_data_addins"),

# Check if the username already exists for AddInstructor form
    path('addins/inputcheck',views.inputcheckfun,name="inputcheck"),

# Search functionality in Add/Update Instructor page 
    path('addins/exact_url',views.your_view,name="exact_url"),

# Data displayed in  Add/Update Instructor page for edit/update functionality
    path('addins/view_data_aj',views.viewdataajfun,name="view_data_aj"),

# Update functionality in Add/Update Instructor page
    path('addins/update_aj',views.update_ajfun,name="update_aj"),

# Add/Update Instructor html page Ends


    path('addstu/',views.addstudent,name="addstu"),

    path('createcourse/',views.createcourse,name="createcourse"),
    path('createcourse/dis_data_createcourse',views.coursedataajfun,name="dis_data_createcourse"),
    path('createcourse/search_course',views.searchcourse,name="search_course"),
    
    # Data displayed in  Create/Update Course page for edit/update functionality
    path('createcourse/view_course_data_aj',views.viewcoursedataajfun,name="view_course_data_aj"),
    
    # Display the csm table in admin module
    # path('createcourse/display_csmtable',views.csmajfun,name="display_csmtable"),


    # Assign student to course
    path('createcourse/assign_student_csm',views.assign_student,name="assign_student_csm"),


    path('inscal',views.instructorcalendar,name="inscal"),
    path('insformsubmit',views.addinstructorform,name="insformsubmit"),
    
    path('addcourse',views.addcourseform,name="addcourse"),
    path('loginform',views.loginfun,name='loginform'),
    path('logout',views.logoutfun,name="logout"),
    # Check if the username already exists for AddInstructor form
    path('addins/inputcheck',views.inputcheckfun,name="inputcheck"),
    path('addins/exact_url',views.your_view,name="exact_url"),
    path('addins/view_data_aj',views.viewdataajfun,name="view_data_aj"),
    path('addins/update_aj',views.update_ajfun,name="update_aj"),
# Check if the username already exists for AdddStudent form
    path('addstu/inputcheck',views.stu_form_inputcheckfun,name="inputcheck"),

    
    
    
  
    
    

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