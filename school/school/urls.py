"""school URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from officer import views
from officer.views import AssignTeacherView, AssignTeacherDetailView
#from teacher import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', include('officer.urls')),
    path('register/', views.register, name='register_page'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/teacher/', views.registerTeacher, name='register_teacher_page'),
    path('create/grade/', views.createGrade, name='create_grade'),
    path('create/course/', views.createCourse, name='create_course'),
    path('teacher/assign/', AssignTeacherView.as_view(), name='assign_teacher'),
    path('teacher/assign/detail/', AssignTeacherDetailView.as_view(), name='assign_teacher_detail'),
]
