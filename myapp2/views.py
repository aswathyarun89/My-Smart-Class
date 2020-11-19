from django.shortcuts import render
from django.shortcuts import redirect, render

# Create your views here.
def myfunction(request):
    return render(request, 'index.html')
def dashboard(request):
    return render(request, 'admin/Admindashboard.html')
def addinstructor(request):
    return render(request, 'admin/AddUpdateInstructor.html')
def addstudent(request):
    return render(request, 'admin/AddUpdateStudent.html')
def createcourse(request):
    return render(request, 'admin/CreateCourses.html')
def instructorcalendar(request):
    return render(request, 'admin/InstructorCalender.html')


def dashboard1(request):
  if request.method == 'GET':
     ...
     # your code lies here when request is GET
     return render(request, 'admin/admindashboard.html')
  else:
     return redirect('dashboard1')