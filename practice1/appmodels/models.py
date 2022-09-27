from unittest.util import _MAX_LENGTH
from django.db import models
import uuid
from django.contrib.auth.models import User
# from datetime import datetime    
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    # is_student = models.BooleanField(default=False)
    # is_teacher = models.BooleanField(default=False)
    mobile_no = models.CharField(max_length=10, null=True)
    address= models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.username


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    reqister_number = models.CharField(max_length=20, null=True, blank=True)
    college_name = models.CharField(max_length=50, null=True, blank=True)

    # def __str__(self):
    #     return self.user.firstname +''+self.user.lastname

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    qualification = models.CharField(max_length=20, null=False, blank=False)
    position = models.CharField(max_length=20)
    # subject_id = models.ManyToManyField(Subject)

    # def __str__(self):
    #     return self.user

class Subject(models.Model):
    subject_id = models.CharField(max_length=20, primary_key=True)
    subject_name = models.CharField(max_length=30, null=False, blank=False)
    # Teacher_id = models.ForeignKey('Teacher', on_delete=models.SET_NULL, null=True, blank=True)
    teacher_id = models.ManyToManyField(Teacher)

    def __str__(self):
        return self.subject_name



class Set(models.Model):
    set_id = models.CharField(max_length=20, primary_key=True)
    set_name = models.CharField(max_length=20, null=False, blank=False)
    # Teacher_id = models.ForeignKey('Teacher', on_delete=models.SET_NULL, null=True, blank=True)
    subject_id = models.ForeignKey('Subject', on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.set_name

class Question(models.Model):
    question_id = models.CharField(max_length=20, primary_key=True)
    question_name = models.TextField(max_length=10000, null=False, blank=False)
    option1=models.CharField(max_length=200)
    option2=models.CharField(max_length=200)
    option3=models.CharField(max_length=200)
    option4=models.CharField(max_length=200)
    subject_id = models.ForeignKey('Subject', on_delete=models.CASCADE, null=True, blank=True)
    # set_id = models.ForeignKey('Set', on_delete=models.SET_NULL, null=True, blank=True)

    options=(('Option1','Option1'),('Option2','Option2'),('Option3','Option3'),('Option4','Option4'))
    answer=models.CharField(max_length=200,choices=options)

    def __str__(self):
        return self.question_name   


class SetQuestionNumber(models.Model):
    # id =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    set_question_id = models.CharField(max_length=20, primary_key=True)
    question_id = models.ForeignKey('Question', on_delete=models.SET_NULL, null=True, blank=True)
    set_id = models.ManyToManyField(Set)

    def __str__(self):
        return self.set_question_id    


class ExamAttemptDetail(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_answer = models.CharField(max_length=1000, null=True, blank=False)
    set_question_id = models.ForeignKey('SetQuestionNumber', on_delete=models.SET_NULL, null=True, blank=True)
    student_id = models.ForeignKey('Student', on_delete=models.CASCADE)
    total_time = models.IntegerField(null=False, blank=False)

    


class Evaluation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    total_marks = models.IntegerField(null=False, blank=False)
    score = models.IntegerField(null=False, blank=False)
    result = models.BooleanField(default=False)
    student_id = models.ForeignKey('Student', on_delete=models.CASCADE)





















































































# class User(AbstractUser):
#     pass


# class Student(models.Model):
#     student_id =models.CharField(max_length=20,primary_key=True)
#     user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
#     reqister_number = models.CharField(max_length=20, null=True, blank=True)
#     college_name = models.CharField(max_length=50, null=True, blank=True)



# class Master(models.Model):
#     master_id = models.CharField(max_length=20, primary_key=True)
#     user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
#     qualification =models.CharField(max_length=20, null=False, blank=False)
#     position = models.CharField(max_length=20)

    

# class Subject(models.Model):
#     subject_id = models.CharField(max_length=20, primary_key=True)
#     subject_name = models.CharField(max_length=30, null=False, blank=False)



# class Set(models.Model):
#     set_id = models.CharField(max_length=20, primary_key=True)
#     set_name = models.CharField(max_length=20, null=False, blank=False)
#     master_id= models.ForeignKey('Master',on_delete=models.SET_NULL, null=True, blank=True)
#     subject_id = models.ForeignKey('Subject',on_delete=models.SET_NULL, null=True, blank=True)



# class Question(models.Model):
#     question_id = models.CharField(max_length=20, primary_key=True)
#     question_name = models.TextField(max_length=10000, null=False,blank=False)
#     answer = models.TextField(max_length=100, null=False,blank=False)
#     subject_id = models.ForeignKey('Subject',on_delete=models.SET_NULL, null=True, blank=True)
#     set_id = models.ForeignKey('Set',on_delete=models.SET_NULL, null=True, blank=True)



# class SetQuestionNumber(models.Model):
#     # id =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     set_question_id= models.CharField(max_length=20, primary_key=True)
#     question_id = models.ForeignKey('Question',on_delete=models.SET_NULL, null=True, blank=True)
#     set_id = models.ManyToManyField(Set)


# class Option(models.Model):
#     option_id = models.CharField(max_length=20, primary_key=True)
#     choice_a = models.CharField(max_length=1000, null=False, blank=False)
#     choice_b = models.CharField(max_length=1000, null=False, blank=False)
#     choice_c = models.CharField(max_length=1000, null=False, blank=False)
#     choice_d = models.CharField(max_length=1000, null=False, blank=False)
#     question_id = models.ForeignKey('Question',on_delete=models.SET_NULL, null=True, blank=True)


# class ExamAttemptDetail(models.Model):
#     id =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     user_answer = models.CharField(max_length=1000, null=True, blank=False)
#     set_question_id = models.ForeignKey('SetQuestionNumber',on_delete=models.SET_NULL, null=True, blank=True)
#     student_id = models.ForeignKey('Student',on_delete=models.CASCADE)
#     # start_time = models.DateTimeField(default=datetime.now)
#     # end_time = models.DateTimeField(default=datetime.now)
#     total_time=models.IntegerField(null=True,blank=True)


# class Evaluation(models.Model):
#     id =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     total_marks =models.IntegerField(null=False,blank=False)
#     score = models.IntegerField(null=False,blank=False)
#     result = models.BooleanField(default=False)
#     student_id = models.ForeignKey('Student',on_delete=models.CASCADE)

