from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.urls import reverse
from Notes.models import *
from Notes.forms import *

# Create your views here.
def Index(request):
    return render(request, 'Dash.html')

#Admin login
def AdminLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # Assuming 'username' is the name of the input field for username
        password = request.POST.get('InputPassword')
        print("Username:", username)
        print("Password:", password)
        user = authenticate(username=username, password=password)  # Use 'username' instead of 'email'
        print("User:", user)
        if user is not None:
            if user.is_superuser:
                login(request, user)
                return HttpResponseRedirect(reverse('customadmin:dashboard'))
            else:
                messages.error(request, 'You must be a SuperUser to login')
                print("You must be superuser")
        else:
            messages.error(request, 'Invalid username or password')
            print("Invalid username or password")

    return render(request, 'Login.html')
#admin logout
def Admin_Logout(request):
    
    logout(request)
    return HttpResponseRedirect(reverse('customadmin:admin-login'))

#Semester
def Semester_Detail(request):
    sem=Semester.objects.all()
    return render(request,'Sem.html',{'sem':sem})

def Add_Semester(request):
    if request.method=='POST':
        fm=SemesterForm(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect(reverse('customadmin:semester-detail'))
    else:
        fm=SemesterForm()
    return render(request,'Addsemester.html',{'fm':fm})


#Subject
def Subject_Detail(request):
    sub=Subject.objects.all()
    return render(request,'Subject.html',{'sub':sub})

def Add_Subject(request):
    if request.method=='POST':
        fm=SubjectForm(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect(reverse('customadmin:subject-detail'))
    else:
        fm=SubjectForm()
    return render(request,'Addsubject.html',{'fm':fm})


def Chapter_Detail(request):
    Chap=Chapter.objects.all()
    return render(request,'Chapterdet.html',{'Chap':Chap})

def Add_Chapter(request):
    if request.method=='POST':
        fm=ChapterForm(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect(reverse('customadmin:chapter-detail'))
    else:
        fm=ChapterForm()
    return render(request,'Addchapter.html',{'fm':fm})


def Notes_Detail(request):
    notes=Notes.objects.all()
    return render(request,'Notesdet.html',{'notes':notes})

def Add_Notes(request):
    if request.method=='POST':
        fm=NotesForm(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect(reverse('customadmin:notes-detail'))
    else:
        fm=NotesForm()
    return render(request,'Addnote.html',{'fm':fm})
    


