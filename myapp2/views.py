from django.shortcuts import render,redirect
from .models import *
from random import random
from django.core.files.storage import FileSystemStorage
import datetime
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from itertools import chain
from operator import attrgetter
from django.core import serializers
from django.db.models import Value as V
from django.db.models.functions import Concat 
from django.db.models import Prefetch
import json
import collections


# Create your views here.

def myfunction(request):
    return render(request, 'index.html')

# Add update instructor html page
def addinstructor(request):
    if not request.session.get('iden_key', None):
        return render(request,'index.html')
    else:
        v_profile=request.session['iden_key']
        profile=User_Cred.objects.get(id=v_profile)
        # v_display=User_Cred.objects.filter(User_Type="Instructor")
        # return render(request, 'Administrator/AddUpdateInstructor.html',{'data':profile,'display':v_display})
        return render(request, 'Administrator/AddUpdateInstructor.html',{'data':profile})

# Add update instructor html page displaying the user details already added
def displaydataajfun(request):
    v_display=User_Cred.objects.filter(User_Type="Instructor")
    # a=User_Info.objects.all()
    # data=[{'iden1':i.User_Reg_No,'iden2':i.First_Name,'iden3':i.Last_Name,'iden4':i.Email}for i in a]
    data=[{'iden1':i.User_Reg_No.User_Reg_No,'iden2':i.User_Reg_No.First_Name,'iden3':i.User_Reg_No.Last_Name,'iden4':i.User_Reg_No.Email}for i in v_display]
    return JsonResponse({'key':data})

# Add instructor form in Add update instructor html page(Admin module)
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
        return redirect('addins')       
    else:
        return render(request,'Administrator/AddUpdateStudent.html')

# Add instructor form in Add update instructor html page(Admin module)
# Check if the username already exists
@csrf_exempt        
def inputcheckfun(request):
    y=request.POST['name']        
    try:
        x= User_Cred.objects.get(User_Id=y)        
        return JsonResponse({'error':'Username already exists'})                                           
    except User_Cred.DoesNotExist:
        return JsonResponse({'error':''})

# Search function in the admin module in(Add update instructor html page)
@csrf_exempt     
def your_view(request):
    if (request.method=="POST"):
        v_profile=request.session['iden_key']
        profile=User_Cred.objects.get(id=v_profile)        
        search_text=request.POST['name']        
        try:           
            records=User_Cred.objects.filter(User_Type="Instructor").select_related('User_Reg_No').filter(Q(User_Reg_No__First_Name__icontains=search_text)|Q(User_Reg_No__Last_Name__icontains=search_text)|Q(User_Reg_No__Email__iexact=search_text))               
            if records==[]:
                return redirect('addins')            
            else:
                data=[{'key1':i.User_Reg_No.User_Reg_No,'key2':i.User_Reg_No.First_Name,'key3':i.User_Reg_No.Last_Name,'key4':i.User_Reg_No.Email}for i in records]
                
                return JsonResponse({'key_id':data})
                # return render(request,'Administrator/AddUpdateInstructor.html',{'myitem':records,'data':profile})
        except User_Info.DoesNotExist:
            return redirect('addins')
    else:
        records = []
        return render(request, 'Administrator/AddUpdateInstructor.html')


# Data view in Add update instructor html page
@csrf_exempt
def viewdataajfun(request):
    v_view=request.POST['view_id']
    single_data=User_Info.objects.get(User_Reg_No=v_view)
    single_data_cred=User_Cred.objects.get(User_Reg_No=v_view)   
    data=[{'data1':single_data.User_Reg_No,'data2':single_data.First_Name,'data3':single_data.Last_Name,'data4':single_data.Email,'data5':single_data.Mobile_No,'data6':single_data.Address,'data7':single_data.Status,'data8':single_data.User_Joining_Date,'data9':single_data.User_Photo}]
    data_cred=[{'data_cred_1':single_data_cred.User_Id,'data_cred_2':single_data_cred.Password,'data_cred_3':single_data_cred.User_Type}]
    return JsonResponse({'key':data,'key1':data_cred})

# Data upate in Add update instructor html page starts in admin module
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
    v_joining_date = request.POST['user_join_date']       
    User_Info.objects.filter(User_Reg_No=v_updateid).update(First_Name=v_first_name,Last_Name=v_last_name,Email=v_email,Mobile_No=v_mob_no,Address=v_address,Status=v_status,User_Joining_Date=v_joining_date,User_Reg_Date=reg_date)
    User_Cred.objects.filter(User_Reg_No=v_updateid).update(Password=v_password)        
    return JsonResponse({'key_update':'Update successfully completed! Click on OK to continue'})

# Add update student html page in admin module
def addstudent(request):
    if not request.session.get('iden_key', None):
        return render(request,'index.html')
    else:
        v_profile=request.session['iden_key']
        profile=User_Cred.objects.get(id=v_profile)
        v_display=User_Info.objects.all()
        return render(request, 'Administrator/AddUpdateStudent.html',{'display':v_display,'data':profile})

# Add student form in Add update instructor html page(Admin module)
# Check if the username already exists
@csrf_exempt        
def stu_form_inputcheckfun(request):
    y=request.POST['name']        
    try:
        x= User_Cred.objects.get(User_Id=y)        
        return JsonResponse({'error':'Username already exists'})                                           
    except User_Cred.DoesNotExist:
        return JsonResponse({'error':''})

# Create Update Course html page in admin module
def createcourse(request):
    if not request.session.get('iden_key', None):
        return render(request,'index.html')
    else:
        v_profile=request.session['iden_key']
        profile=User_Cred.objects.get(id=v_profile)
        course_owner_name=User_Cred.objects.filter(User_Type="Instructor").prefetch_related(Prefetch('User_Reg_No',queryset=User_Info.objects.annotate(full_name=Concat('First_Name', V(' '),'Last_Name'))))       
        course_student_name = User_Cred.objects.filter(User_Type="Student").prefetch_related(Prefetch('User_Reg_No',queryset=User_Info.objects.annotate(full_name=Concat('First_Name', V(' '),'Last_Name'))))   
        return render(request, 'Administrator/CreateCourses.html',{'data':profile,'selectedvalue':course_owner_name,'c_student_name':course_student_name})

# Display the course details for which the course owners are Instructors
def coursedataajfun(request):   
    course_data=Course_Info.objects.all().select_related('Course_Owner_Id')
    data=[{'iden1':i.Course_Id,'iden2':i.Course_Name,'iden3':i.Course_Duration,'iden4':i.Course_Owner}for i in course_data]    
    return JsonResponse({'key':data})

# Add course form in Add update instructor html page(Admin module)
def addcourseform(request):    
    if (request.method=="POST"):
        course_name = request.POST['coursename']
        course_owner_name= request.POST.get('courseowner')        
        course_owner=course_owner_name.split(' ')[0]
        course_duration = request.POST['courseduration']
        course_details = request.POST['coursedetails']
        course_start_date=request.POST['CourseStartDate']
        course_end_date=request.POST['CourseEndDate']
        course_myfile=request.FILES['CourseLogoPic']
        course_file_name=str(random())+course_myfile.name
        fs=FileSystemStorage()
        fs.save(course_file_name,course_myfile)
        obj1=User_Info.objects.get(First_Name=course_owner)            
        Course_Info_obj=Course_Info(Course_Owner_Id=obj1,Course_Name=course_name,Course_Owner=course_owner,Course_Duration=course_duration,Course_Descrp=course_details,Course_StartDate=course_start_date,Course_EndDate=course_end_date,Course_Logo=course_file_name)
        Course_Info_obj.save()
        return redirect('createcourse')        
    else:
        return render(request,'Administrator/AddUpdateStudent.html')

# Search function in the admin module in(Create/Update course html page)
@csrf_exempt     
def searchcourse(request):
    if (request.method=="POST"):
        v_profile=request.session['iden_key']
        profile=User_Cred.objects.get(id=v_profile)        
        search_text=request.POST['name']        
        try:           
            c_data=Course_Info.objects.filter(Q(Course_Name__icontains=search_text)|Q(Course_Id__icontains=search_text))               
            if c_data==[]:
                return redirect('createcourse')            
            else:
                data=[{'key1':i.Course_Id,'key2':i.Course_Name,'key3':i.Course_Duration,'key4':i.Course_Owner}for i in c_data]               
                return JsonResponse({'key_course':data})
        except User_Info.DoesNotExist:
            return redirect('addins')
    else:
        c_data = []
        return render(request, 'Administrator/AddUpdateInstructor.html')

@csrf_exempt
def viewcoursedataajfun(request):
    v_view=request.POST['view_id']
    #  v_courseid=request.POST['cid']
    single_data=Course_Info.objects.get(Course_Id=v_view)
    # course_owner_name=User_Cred.objects.filter(User_Type="Instructor").prefetch_related(Prefetch('User_Reg_No',queryset=User_Info.objects.annotate(full_name=Concat('First_Name', V(' '),'Last_Name'))))  
    csm_obj=Course_Student_Map.objects.filter(Course_Id=v_view)
    CourseDetails=[{'data1':single_data.Course_Id,'data2':single_data.Course_Name,'data3':single_data.Course_Owner,'data4':single_data.Course_Duration,'data5':single_data.Course_Descrp,'data6':single_data.Course_Logo}]       
    csm_table_data=[{'td1':x.User_Reg_No_id,'td2':x.User_Reg_No.First_Name,'td3':x.User_Reg_No.Last_Name}for x in csm_obj]
   
    print(csm_obj)
    return JsonResponse({'key_course':CourseDetails,'table_key':csm_table_data})
    # return JsonResponse({'key_course':CourseDetails})

@csrf_exempt  
def assign_student(request):
    try:
        CSM_Id_last_entry = Course_Student_Map.objects.latest('CSM_Id')        
    except:
        csmid = 101
    else:
        csmid = CSM_Id_last_entry.CSM_Id+1    
    crs_id=request.POST.get('c_id')       
    crs_student_id=request.POST['stu_id']
    crs_assigned_date = datetime.datetime.now()
    crs_status="Assigned"
    crs_progress=0
    try:
        verify=Course_Student_Map.objects.get(Course_Id=crs_id,User_Reg_No=crs_student_id)
        print(verify)
    except:
        course_info_pk=Course_Info.objects.get(Course_Id=crs_id)
        user_info_pk=User_Info.objects.get(User_Reg_No=crs_student_id)
        Course_Student_Map_Obj=Course_Student_Map(CSM_Id=csmid,Course_Id_id=course_info_pk.Course_Id,User_Reg_No_id=user_info_pk.User_Reg_No,Assigned_Date=crs_assigned_date,CSM_Status=crs_status,Course_Progress=crs_progress)
        Course_Student_Map_Obj.save()
        return JsonResponse({'alert':'Data Sucessfully added','Ref_crsid':crs_id})
    else:        
        return JsonResponse({'alert':'Student already added'})
        


    # course_info_pk=Course_Info.objects.get(Course_Id=crs_id)
    # user_info_pk=User_Info.objects.get(User_Reg_No=crs_student_id)
    # Course_Student_Map_Obj=Course_Student_Map(CSM_Id=csmid,Course_Id_id=course_info_pk.Course_Id,User_Reg_No_id=user_info_pk.User_Reg_No,Assigned_Date=crs_assigned_date,CSM_Status=crs_status,Course_Progress=crs_progress)
    # Course_Student_Map_Obj.save()
    # return JsonResponse({'alert':'Data Sucessfully added','Ref_crsid':crs_id})

# @csrf_exempt  
# def csmajfun(request):
#     v_courseid=request.POST['cid']
#     print(v_courseid)
#     csm_obj=Course_Student_Map.objects.filter(Course_Id=v_courseid)
#     print(csm_obj)
#     csm_table_data=[{'td1':x.User_Reg_No_id,'td2':x.User_Reg_No.First_Name}for x in csm_obj]
#     print(csm_table_data)
#     return JsonResponse({'table_key':csm_table_data})



    














# instructor calendar page in admin module
def instructorcalendar(request):
    if not request.session.get('iden_key', None):
        return render(request,'index.html')
    else:
        v_profile=request.session['iden_key']
        profile=User_Cred.objects.get(id=v_profile)
        course_data=Course_Info.objects.all()
        return render(request, 'Administrator/InstructorCalender.html',{'data':profile,'course_display':course_data})





        








    #  Instructor Module

def addstudentinspage(request):
    if not request.session.get('iden_key', None):
        return render(request,'index.html')
    else:
        v_profile=request.session['iden_key']
        profile=User_Cred.objects.get(id=v_profile)
        v_display=User_Cred.objects.filter(User_Type="Student")
        return render(request, 'Instructor/AddUpdateStudent.html',{'data':profile,'display':v_display})
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

def logoutfun(request):
    if not request.session.get('iden_key', None):
        return render(request,'index.html')
    else:
        del request.session['iden_key']
        return render(request,'index.html')





