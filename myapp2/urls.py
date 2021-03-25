from django.urls import path
from . import views
urlpatterns = [

# Loading the index page
    path('',views.myfunction,name="pgm"),

# Login form
    path('loginform',views.loginfun,name='loginform'),

# Logout form
    path('logout',views.logoutfun,name="logout"),

        # Admin Module Path starts

# Loading the admindashbaord html page
    path('admindashboard/',views.dashboard,name="admindashboard"),

        # Add/Update Instructor html page begins

# Add/Update Instructor html page with displaying the page except the Userdetails
    path('addins/',views.addinstructor,name="addins"),

# Add/Update Instructor html page with displaying the page with userdetails
    path('addins/dis_data_addins',views.displaydataajfun,name="dis_data_addins"),

# Add/Update Instructor html page with adding a new instructor
    path('addins/insformsubmit',views.addinstructorform,name="insformsubmit"),

# Check if the username already exists for AddInstructor form
    path('addins/inputcheck',views.inputcheckfun,name="inputcheck"),

# Search functionality in Add/Update Instructor page 
    path('addins/exact_url',views.your_view,name="exact_url"),

# Data displayed in  Add/Update Instructor page for edit/update functionality
    path('addins/view_data_aj',views.viewdataajfun,name="view_data_aj"),

# Update functionality in Add/Update Instructor page
    path('addins/update_aj',views.update_ajfun,name="update_aj"),

        # Add/Update Instructor html page Ends

        # Add/Update Student html page begins

# Add/Update Student html page with displaying the page except the Student details
    path('addstu/',views.addstudent,name="addstu"),

# Add/Update Student html page with displaying the page with student details
    path('addstu/display_studentdata',views.displaystudentdataajfun,name="display_studentdata"),
    

# Add Student form in Admin module
    path('addstu/stuformsubmit',views.studentformfun,name="stuformsubmit"),

# Check if the username already exists for AdddStudent form
    path('addstu/inputcheck',views.stu_form_inputcheckfun,name="inputcheck"),

# Search Student functionality in Admin Module
    path('addstu/searchstudent',views.searchstudentfunction,name="searchstudent"), 

# View Student data in Admin Module
    path('addstu/viewstudentdata_aj',views.viewstudentdatafunction,name="viewstudentdata_aj"),

# Update Student data in Admin Module
    path('addstu/updatestudent_aj',views.updatestudentdatafunction,name="updatestudent_aj"),

        # Add/Update Student html page ends

        # Add/Update Course html page starts

# Add/Update Course html page with displaying the page except the course details
    path('createcourse/',views.createcourse,name="createcourse"),

# Display Course data in Add/Update Course html page in Admin Module
    path('createcourse/dis_data_createcourse',views.coursedataajfun,name="dis_data_createcourse"),

# Add Course form in Admin module
     path('createcourse/addcrsform',views.addcourseform,name="addcrsform"),

# Search functionality in Add/Update Course html page
    path('createcourse/search_course',views.searchcourse,name="search_course"),
    
# Data displayed in  Create/Update Course page for edit/update functionality
    path('createcourse/view_course_data_aj',views.viewcoursedataajfun,name="view_course_data_aj"),
    
# Assign student to course in Add/Update Course html page
    path('createcourse/assign_student_csm',views.assign_student,name="assign_student_csm"),

        # Add/Update Course html page ends

        # View Instructor calender starts in Admin Module starts
        
# Loading the instructor calender in Admin Module
    path('inscal',views.instructorcalendar,name="inscal"),

        # Admin Module Path Ends

        # Instructor Module path starts
# Instructor dashboard in Instructor module 
    path('insdashboard/', views.instructordashboard, name='insdashboard'),

        # Add/Update Student html page in Instructor Module starts

# Add/Update Student html page with displaying the page except the studentdetails in Instructor Module
    path('addstuins/',views.addstudentinspage,name="addstuins"),

# Add/Update InstrStudentuctor html page with displaying the page with studentdetails Instructor Module
    path('addstuins/display_studentdata',views.displaystudentdataajfun,name="display_studentdata"),

# Add Student form in Instructor module
    path('addstuins/stuformsubmit',views.studentformfun,name="stuformsubmit"),

# Check if the username already exists for AdddStudent form
    path('addstuins/inputcheck',views.stu_form_inputcheckfun,name="inputcheck"),

# Search functionality in Add/Update Student page in Instructor Module
     path('addstuins/searchstudent',views.searchstudentfunction,name="searchstudent"),

# View Student data in Instructor Module
    path('addstuins/viewstudentdata_aj',views.viewstudentdatafunction,name="viewstudentdata_aj"),

# Update Student data in Instructor Module
    path('addstuins/updatestudent_aj',views.updatestudentdatafunction,name="updatestudent_aj"),

        # Add/Update Student html page in Instructor Module ends

        # Create Course html page in Instructor Module Starts

#Loding the createcourse page in instructor module
    path('createcourseins/',views.createcourseinspage,name="createcourseins"),

    # Display Course data in Add/Update Course html page in Admin Module
    path('createcourseins/dis_data_createcourse',views.coursedataajfun,name="dis_data_createcourse"),

# Add Course form in Admin module
     path('createcourseins/addcrsform',views.addcourseform,name="addcrsform"),

# Search functionality in Add/Update Course html page
    path('createcourseins/search_course',views.searchcourse,name="search_course"),
    
# Data displayed in  Create/Update Course page for edit/update functionality
    path('createcourseins/view_course_data_aj',views.viewcoursedataajfun,name="view_course_data_aj"),
    
# Assign student to course in Add/Update Course html page
    path('createcourseins/assign_student_csm',views.assign_student,name="assign_student_csm"),

        # Add/Update Course html page in Instructor Module ends


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