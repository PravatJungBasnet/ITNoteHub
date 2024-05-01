from django.contrib import admin
from .models import Faculty,Semester,Subject,Notes,Chapter,Contact_Us

# Register your models here.
@admin.register(Faculty)




class FacultyAdmin(admin.ModelAdmin):
    list_display=['name']


@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display=['name','faculty']

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display=['name','semester']

@admin.register(Notes)
class NotesAdmin(admin.ModelAdmin):
    list_display=['title','faculty','semester','subject','chapter']
    
@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display=['unit','title','subject']

@admin.register(Contact_Us)
class Contact_UsAdmin(admin.ModelAdmin):
    list_display=['name','email','subject','message']




