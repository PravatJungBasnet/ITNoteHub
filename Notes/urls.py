from django.urls import path
from . import views
urlpatterns =[
    path('',views.Index,name='index'),
    path('index', views.IndexView.as_view(), name='index'),
    path('about/',views.About, name='about'),
    path('contact/',views.Contact, name='contact'),
    path('csit/',views.CSIT, name='csit'),
    path('bca/',views.BCA, name='bca'),
    path('bit/',views.BIT, name='bit'),
    path('<str:name>/semester/<int:id>/', views.SemesterDetails, name='semester_details'),

    #path('semester/<int:id>/',views.SemesterDetails,name='semester'),
    #path('semesters/<int:pk>/',views.SemesterDetailView.as_view(), name='semester'),
    path('subject<int:id>/',views.SubjectDetails,name='subject'),
    path('chapters<int:id>/',views.ChapterDetails,name='chapters'),
    path('notes/<int:id>/',views.NoteView,name='notes')
    
       
    
]
