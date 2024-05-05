from django.urls import path
from . import views
app_name = 'customadmin'
urlpatterns=[
    path('', views.AdminLogin,name='admin-login'),
    path('admin-logout/',views.Admin_Logout,name='admin-logout'),
    path('dashboard/', views.Index,name='dashboard'),
    path('sem/',views.Semester_Detail,name='sem'),
    path('subject/',views.Subject_Detail,name='subject'),
    path('chapterdetails/',views.Chapter_Detail,name='chapterdetails'),
    path('notesdetails/', views.Notes_Detail,name='notesdetails')
    
    
]