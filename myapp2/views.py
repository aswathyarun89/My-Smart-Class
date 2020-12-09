from django.shortcuts import render
# from django.shortcuts import redirect, render

# Create your views here.
def myfunction(request):
    return render(request, 'index.html')
def dashboard(request):
    return render(request, 'Administrator/Admindashboard.html')
def addinstructor(request):
    return render(request, 'Administrator/AddUpdateInstructor.html')
def addstudent(request):
    return render(request, 'Administrator/AddUpdateStudent.html')
def createcourse(request):
    return render(request, 'Administrator/CreateCourses.html')
def instructorcalendar(request):
    return render(request, 'Administrator/InstructorCalender.html')



# def dashboard1(request):
#   if request.method == 'GET':
#      ...
#      # your code lies here when request is GET
#      return render(request, 'admin/admindashboard.html')
#   else:
#      return redirect('dashboard1')

    #  Instructor Module

def addstudentinspage(request):
    return render(request, 'Instructor/AddUpdateStudent.html')
def createcourseinspage(request):
    return render(request, 'Instructor/CreateCourses.html')
def instructorcalendarinspage(request):
    return render(request, 'Instructor/InstructorCalender.html')
def assignedcoursesins(request):
    return render(request, 'Instructor/ViewAssignedCourses.html')
def scheduleclass(request):
    return render(request, 'Instructor/ScheduleStartClass.html')
def instructordashboard(request):
    return render(request, 'Instructor/InstructorDashboard.html')
def assignments(request):
    return render(request, 'Instructor/Assignments.html')
def assessments(request):
    return render(request, 'Instructor/Assesments.html')
def documents(request):
    return render(request, 'Instructor/UploadDocuments.html')
def certificate(request):
    return render(request, 'Instructor/Certificate.html')


    #  Student Module

def studentdashboard(request):
    return render(request, 'Student/StudentDashboard.html')
def viewstudentcourse(request):
    return render(request, 'Student/ViewMyCourse.html')
def studentassignment(request):
    return render(request, 'Student/Assignments.html')
def studentassessment(request):
    return render(request, 'Student/Assessments.html')
def studentcertificate(request):
    return render(request, 'Student/Certificate.html')