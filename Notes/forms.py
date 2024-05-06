from django import forms
from .models import Contact_Us,Semester,Chapter,Subject,Notes
class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact_Us
        fields=['name','email','subject','message']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'subject':forms.TextInput(attrs={'class':'form-control'}),
            'message':forms.TextInput(attrs={'class':'form-control'}),
        }
class SemesterForm(forms.ModelForm):
    class Meta:
        model=Semester
        fields=['name','faculty']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'faculty':forms.Select(attrs={'class':'form-control'}),
        }

class SubjectForm(forms.ModelForm):
    class Meta:
        model=Subject
        fields=['name','faculty','semester']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'faculty':forms.Select(attrs={'class':'form-control'}),
           'semester':forms.Select(attrs={'class':'form-control'}),
        }



class ChapterForm(forms.ModelForm):
    class Meta:
        model=Chapter
        fields=['faculty','semester','subject','unit','title',]
        widgets={
            'faculty':forms.Select(attrs={'class':'form-control'}),
            'semester':forms.Select(attrs={'class':'form-control'}),
            'subject':forms.Select(attrs={'class':'form-control'}),
            'unit':forms.TextInput(attrs={'class':'form-control'}),
            'title':forms.TextInput(attrs={'class':'form-control'}),
           
        }

class NotesForm(forms.ModelForm):
    class Meta:
        model=Notes
        fields=['title','faculty','semester','subject','chapter','note']
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'faculty':forms.Select(attrs={'class':'form-control'}),
           'semester':forms.Select(attrs={'class':'form-control'}),
           'subject':forms.Select(attrs={'class':'form-control'}),
           'chapter':forms.TextInput(attrs={'class':'form-control'}),
           'note':forms.FileInput(attrs={'class':'form-control'}),
        }
        
