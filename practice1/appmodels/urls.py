from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [

    path('',views.index),
    # path('user', views.UserList.as_view()),
    # path('user/student', views.StudentList.as_view()),
    # path('user/teacher', views.TeacherList.as_view()),
    # path('user/create', views.UserCreate.as_view()),
    # path('user/student/studentcreate', views.StudentCeate.as_view()),
    # path('user/teacher/teachercreate', views.TeacherCeate.as_view()),
    # path('user/<int:pk>', views.UserDetail.as_view()),
    # path('user/student/<int:pk>', views.StudentDetail.as_view()),
    # path('user/teacher/<int:pk>', views.TeacherDetail.as_view())
    path('user', views.RegisterStudent.as_view()),



]
