from django.shortcuts import render,redirect
from .models import *
from random import random
from django.core.files.storage import FileSystemStorage
import datetime
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q


# from django.shortcuts import redirect, render

# Create your views here.
def myfunction(request):
    return render(request, 'index.html')
def addinstructor(request):
    if not request.session.get('iden_key', None):
        return render(request,'index.html')
    else:
        v_profile=request.session['iden_key']
        profile=User_Cred.objects.get(id=v_profile)
        # profile = User_Cred.objects.select_related('User_Reg_No').filter(User_Reg_No=1000) 
        # for i in profile:
        #     print(i)

        v_display=User_Cred.objects.filter(User_Type="Instructor")
        return render(request, 'Administrator/AddUpdateInstructor.html',{'data':profile,'display':v_display})
@csrf_exempt       
def your_view(request):
    if (request.method=="GET"):
        v_profile=request.session['iden_key']
        profile=User_Cred.objects.get(id=v_profile)
        search_text = request.GET.get('search_box')
        try:
            records=User_Info.objects.filter(First_Name__contains=search_text)
            if records=="":
                return redirect('addins')
            else:
                
                return render(request,'Administrator/AddUpdateInstructor.html',{'myitem':records,'data':profile})
        except User_Info.DoesNotExist:

            return redirect('addins')

    else:
        records = []
        return render(request, 'Administrator/AddUpdateInstructor.html')
# search view function ends

# Data view in update form 
@csrf_exempt
def viewdataajfun(request):
    v_view=request.POST['view_id']
    single_data=User_Info.objects.get(User_Reg_No=v_view)
    single_data_cred=User_Cred.objects.get(User_Reg_No=v_view)
   
    data=[{'data1':single_data.User_Reg_No,'data2':single_data.First_Name,'data3':single_data.Last_Name,'data4':single_data.Email,'data5':single_data.Mobile_No,'data6':single_data.Address,'data7':single_data.Status,'data8':single_data.User_Joining_Date}]
    data_cred=[{'data_cred_1':single_data_cred.User_Id,'data_cred_2':single_data_cred.Password}]
    return JsonResponse({'key':data,'key1':data_cred})
# Data view in update form ends

# Data upate in update form starts
@csrf_exempt
def update_ajfun(request):
    v_updateid=request.POST['update_id']
    v_first_name = request.POST['f_name']
    print(v_first_name)
    v_last_name = request.POST['l_name']
    v_email = request.POST['e_mail']
    v_mob_no = request.POST['mob_no']
    v_address = request.POST['post_ad']
    reg_date = datetime.datetime.now()   
    v_password = request.POST['p_word']
    v_status = request.POST['u_status']
    v_joining_date = request.POST['u_join_date']
    User_Info.objects.filter(User_Reg_No=v_updateid).update(First_Name=v_first_name,Last_Name=v_last_name,Email=v_email,Mobile_No=v_mob_no,Address=v_address,Status=v_status,User_Joining_Date=v_joining_date,User_Reg_Date=reg_date)
    User_Cred.objects.filter(User_Reg_No=v_updateid).update(Password=v_password)    
    return JsonResponse({'key_update':'Update successfully completed! Click on OK to continue'})
# Data update in update form ends


           
    





def addstudent(request):
    if not request.session.get('iden_key', None):
        return render(request,'index.html')
    else:
        v_profile=request.session['iden_key']
        profile=User_Cred.objects.get(id=v_profile)
        v_display=User_Info.objects.all()
        return render(request, 'Administrator/AddUpdateStudent.html',{'display':v_display,'data':profile})
    
def createcourse(request):
    if not request.session.get('iden_key', None):
        return render(request,'index.html')
    else:
        v_profile=request.session['iden_key']
        profile=User_Cred.objects.get(id=v_profile)
        course_data=Course_Info.objects.all()
        return render(request, 'Administrator/CreateCourses.html',{'data':profile,'course_display':course_data})
def instructorcalendar(request):
    return render(request, 'Administrator/InstructorCalender.html')

def addinstructorform(request):
    if (request.method=="POST"):
        name1 = request.POST['firstname']
        name2 = request.POST['lastname']        
        e_mail = request.POST['email']
        mob_no = request.POST['mobileno']
        address1 = request.POST['address']
        user_name = request.POST['username']
        password = request.POST['password']
        join_date = request.POST['joiningdate']
        # reg_No = request.POST['regno']         
        reg_date = datetime.datetime.now()        
        user_status = 'Active'                
        gender = request.POST['gridRadios']
        myfile=request.FILES['fileupload']
        file_name=str(random())+myfile.name
        fs=FileSystemStorage()
        fs.save(file_name,myfile)

        try:
            last_entry = User_Info.objects.latest('User_Reg_No')        
        except:
            reg_No = 1000
        else:
            reg_No = last_entry.User_Reg_No+1

        User_Info_obj=User_Info(First_Name=name1,Last_Name=name2,Email=e_mail,Address=address1,User_Joining_Date=join_date,User_Reg_Date=reg_date,Status=user_status,Gender=gender,Mobile_No=mob_no,User_Reg_No=reg_No,User_Photo=file_name)
        User_Info_obj.save()
        obj=User_Info.objects.latest('User_Reg_No')
        User_Cred_obj = User_Cred(User_Id=user_name,Password=password,User_Type='Instructor',User_Reg_No=obj)
        User_Cred_obj.save()
        return render(request,'Administrator/Admindashboard.html')        
    else:
        return render(request,'Administrator/AddUpdateStudent.html')

# Check if the username already exists

@csrf_exempt        
def inputcheckfun(request):
    y=request.POST['name']        
    try:
        x= User_Cred.objects.get(User_Id=y)        
        return JsonResponse({'error':'Username already exists'})                                           
    except User_Cred.DoesNotExist:
        return JsonResponse({'error':''})

def addcourseform(request):
    if (request.method=="POST"):
        course_name = request.POST['coursename']
        course_owner = request.POST['courseowner']
        course_duration = request.POST['courseduration']
        course_details = request.POST['coursedetails']
        try:
            obj1=User_Info.objects.get(First_Name=course_owner)
            if (obj1.First_Name==course_owner):
                Course_Info_obj=Course_Info(Course_Name=course_name,Course_Owner_Id=obj1,Course_Owner=course_owner,Course_Duration=course_duration,Course_Descrp=course_details)
                Course_Info_obj.save()
                return redirect('createcourse')
                # Need to check this code for course owner is not matching with the entry in Db , need to print a userinterface error
            else:
                return redirect('createcourse')
        except User_Info.DoesNotExist:
                return redirect('createcourse',{'message':'User doesnot exists'})

    else:
        return render(request,'Administrator/AddUpdateStudent.html')





        




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
def assignments(request):
    return render(request, 'Instructor/Assignments.html')
def assessments(request):
    return render(request, 'Instructor/Assesments.html')
def documents(request):
    return render(request, 'Instructor/UploadDocuments.html')
def certificate(request):
    return render(request, 'Instructor/Certificate.html')


    #  Student Module


def viewstudentcourse(request):
    return render(request, 'Student/ViewMyCourse.html')
def studentassignment(request):
    return render(request, 'Student/Assignments.html')
def studentassessment(request):
    return render(request, 'Student/Assessments.html')
def studentcertificate(request):
    return render(request, 'Student/Certificate.html')


# Login Function
def loginfun(request):
    if(request.method=="POST"):
            user_name=request.POST['username']
            password=request.POST['password']
            try:
                x= User_Cred.objects.get(User_Id=user_name)
                if (x.User_Id==user_name and x.Password==password):
                    request.session['iden_key']=x.id
                    
                    if(x.User_Type=='Admin'):
                        return redirect('admindashboard/')
                    elif(x.User_Type=='Instructor'):
                        return redirect('insdashboard/')
                    else:
                        return redirect('studashboard/')                                  
                else:
                    return render(request,'index.html',{'error':'Incorrect Username or Password'})
            except User_Cred.DoesNotExist:
                return render(request,'index.html',{'error':'Incorrect Username or Password'})            

    else:
        return render(request,'index.html')

# Session function

def dashboard(request):
    if not request.session.get('iden_key', None):
        return render(request,'index.html')
    else:
        v_profile=request.session['iden_key']
        profile=User_Cred.objects.get(id=v_profile)
        
        return render(request,'Administrator/Admindashboard.html',{'data':profile})

def logoutfun(request):
    if not request.session.get('iden_key', None):
        return render(request,'index.html')
    else:
        del request.session['iden_key']
        return render(request,'index.html')

def instructordashboard(request):
    if not request.session.get('iden_key', None):
        return render(request,'index.html')
    else:
        v_profile=request.session['iden_key']
        profile=User_Cred.objects.get(id=v_profile)
        return render(request,'Instructor/InstructorDashboard.html',{'data':profile})

def studentdashboard(request):
    if not request.session.get('iden_key', None):
        return render(request,'index.html')
    else:
        v_profile=request.session['iden_key']
        profile=User_Cred.objects.get(id=v_profile)
        return render(request,'Student/StudentDashboard.html',{'data':profile})

# Logout function





