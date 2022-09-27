from django.contrib import admin
from .models import Student, Teacher, Evaluation, ExamAttemptDetail, Set, SetQuestionNumber, Subject, Question
from django.contrib.auth.admin import UserAdmin
from .models import User


admin.site.register(User,UserAdmin)

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Evaluation)
admin.site.register(ExamAttemptDetail)
admin.site.register(Set)
admin.site.register(SetQuestionNumber)
# admin.site.register(Option)
admin.site.register(Subject)
admin.site.register(Question)