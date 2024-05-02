from django import forms
from .models import Contact_Us
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
        
