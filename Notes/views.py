from typing import Any
from django.http import HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.views.generic import DetailView, TemplateView
from .models import *
from django.http import FileResponse
from django.core.mail import send_mail
from django.http import HttpResponse
from .forms import ContactForm
from django.urls import reverse

# Create your views here.
def Index(request):
    return render(request,'index.html')

class IndexView(TemplateView):
    template_name = 'index.html'

def About(request):
    return render(request,'about.html')




def Contact(request):
    if request.method == 'POST':
        contact=ContactForm(request.POST)
        if contact.is_valid():
            name = contact.cleaned_data['name']
            email = contact.cleaned_data['email']
            subject=contact.cleaned_data['subject']
            message = contact.cleaned_data['message']
       
        
        try:
            # Send email
            send_mail(
                subject,
                f"Name: {name}\nEmail: {email}\nMessage: {message}\nSubject: {subject}",
                email,  # Sender's email address
                ['pravatjungbasnet@gmail.com'],  # Recipient's email address
                fail_silently=False,
            )
            contact.save()
            
            # Create an instance of Contact_Us model
           
           
            #Message received! Thank you for contacting us.
            # Save the instance to the database
            

            
            return HttpResponseRedirect(reverse('contact') + '?message=Message%20received!%20Thank%20you%20for%20contacting%20us.')
        except:
            # Inform the user that there's an issue with sending the email
            return HttpResponse('Sorry, there was a problem sending the email. Please try again later.')
    else:
        contact=ContactForm()
    return render(request, 'contact.html',{'contact':contact})


def CSIT(request):
    return render(request,'CSIT.html')
def BCA(request):
    return render(request,'BCA.html')

def BIT(request):
    return render(request,'BIT.html')





#Semester 
from django.shortcuts import render
from .models import Faculty, Semester, Subject

def SemesterDetails(request, name,id ):
        # Retrieve the Faculty object based on the provided name
        print('hello')
        faculty = Faculty.objects.get(name=name)
        print(faculty)
        
        # Retrieve the Semester object based on the provided ID
        semester = Semester.objects.get(pk=id)
        
        # Filter subjects based on the semester and faculty
        subjects = Subject.objects.filter(semester=semester, faculty=faculty)
        
        # Render the template with the subjects, semester, and faculty
        return render(request, 'Notes.html', {'subjects': subjects, 'semester': semester, 'faculty': faculty})

#chapters of the subjects  class based
class ChapterDetailView(DetailView):
    model=Chapter
    template_name='Chapter.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        subject=self.get_object()
        kwargs["chapters"]=Chapter.objects.filter(subject=subject)
        return super().get_context_data(**kwargs)





    
    
   



class SemesterDetailView(DetailView):
    model = Semester
    template_name = 'Notes.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        semester = self.get_object()
        kwargs["subjects"] = Subject.objects.filter(semester=semester)
        return super().get_context_data(**kwargs)


def SubjectDetails(request,id):
    subject=Subject.objects.get(id=id)
    notes=Notes.objects.filter(subject=subject)
    return render(request,'Notes.html',{'subject':subject,'notes':notes})


# ig gives the chapter of the releated subject 
def ChapterDetails(request,id):
    subject=Subject.objects.get(pk=id)
    chapters=Chapter.objects.filter(subject=subject)
    return render(request,'Chapter.html',{'subject':subject,'chapters':chapters})






# notes view
def NoteView(request,id):
    chapters=Chapter.objects.get(pk=id)
    notes=Notes.objects.get(chapter=chapters)
    response=FileResponse(notes.note,content_type='application/pdf')
    return response




    








