from django.db import models

# Create your models here.
class Faculty(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
       return self.name

class Semester(models.Model):
    semester_choice=[
        ('First Semester','First Semester'),
        ('Second_Semester','Second Semester'),
        ('Third Semester','Third Semester'),
        ('Fourth Semester','Fourth Semester'),
        ('Fifth Semester','Fifth Semester'),
        ('Sixth Semester','Sixth Semester'),
        ('Seventh Semester','Seventh Semester'),
        ('Eigth Semester','Eight Semester'),
    ]
    name=models.CharField(choices= semester_choice,max_length=100)
    faculty=models.ForeignKey(Faculty,on_delete=models.CASCADE)
    def __str__(self):
       return self.name

class Subject(models.Model):
    name=models.CharField(max_length=100)
    faculty=models.ForeignKey(Faculty,on_delete=models.CASCADE)
    semester=models.ForeignKey(Semester,on_delete=models.CASCADE)
    def __str__(self):
       return self.name
    
class Chapter(models.Model):
    Unit_choice=[
        ('Unit 1','Unit 1'),
        ('Unit 2','Unit 2'),
        ('Unit 3','Unit 3'),
        ('Unit 4','Unit 4'),
        ('Unit 5','Unit 5'),
        ('Unit 6','Unit 6'),
        ('Unit 7','Unit 7'),
        ('Unit 8','Unit 8'),
    ]
    faculty=models.ForeignKey(Faculty,on_delete=models.CASCADE)
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    semester=models.ForeignKey(Semester,on_delete=models.CASCADE)
    unit=models.CharField(max_length=100,choices=Unit_choice)
    title=models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.title


class Notes(models.Model):
    title=models.CharField(max_length=100)
    faculty=models.ForeignKey(Faculty,on_delete=models.CASCADE)
    semester=models.ForeignKey(Semester,on_delete=models.CASCADE)
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    chapter=models.ForeignKey(Chapter,on_delete=models.CASCADE)
    note=models.FileField(upload_to='pdf')

    def __str__(self):
       return  self.title
    

class Contact_Us(models.Model):
    name=models.CharField(max_length=100,blank=False)
    email=models.EmailField(max_length=100,blank=False)
    subject=models.CharField(max_length=100,blank=False)
    message=models.TextField(max_length=1000,blank=False)

    def __str__(self):
        return self.name

