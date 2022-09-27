from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from appmodels.models import User,Student, Teacher
from appmodels.serializer import UserSerializer, StudentSerializer, TeacherSerializer
from rest_framework.views import APIView
# Create your views here.


def index(request):
    return HttpResponse("<h1>MAJOR PROJECT</h1>")


# class UserList(APIView):
#     def get(self, request):
#         sub = User.objects.all()
#         serializer = UserSerializer(sub, many=True)
#         return Response(serializer.data)


# class UserCreate(APIView):
#     def post(self,request):
#         serializer = UserSerializer(data=request.data)
#         print(serializer)
#         if serializer.is_valid():
#             user= serializer.save()
            
#             return Response(serializer.data)
#         else:
#             print('invalid')
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class UserDetail(APIView):
#     def get_sub_by_pk(self,pk):
#         try:
#             return User.objects.get(pk=pk)

#         except:
#             return Response({
#                 'error': "User does not exist"
#             }, status=status.HTTP_404_NOT_FOUND)


#     def get(self,request,pk):
#         s1 = self.get_sub_by_pk(pk)
#         serializer =UserSerializer(s1)
#         print(serializer)
#         return Response(serializer.data)
  


#     def put(self,request,pk):
#         s1 = self.get_sub_by_pk(pk)
#         serializer =UserSerializer(s1, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#     def delete(self,request,pk):
#         s1 = self.get_sub_by_pk(pk)
#         s1.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class StudentList(APIView):
#     def get(self, request):
#         sub = Student.objects.all()
#         serializer = StudentSerializer(sub, many=True)
#         return Response(serializer.data)


# class StudentCeate(APIView):
#     def post(self,request):
#         serializer = StudentSerializer(data=request.data)
#         print(serializer)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             print('invalid')
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   


# class StudentDetail(APIView):
#     def get_sub_by_pk(self,pk):
#         try:
#             return Student.objects.get(pk=pk)

#         except:
#             return Response({
#                 'error': "Student does not exist"
#             }, status=status.HTTP_404_NOT_FOUND)


#     def get(self,request,pk):
#         s1 = self.get_sub_by_pk(pk)
#         serializer =StudentSerializer(s1)
#         print(serializer)
#         return Response(serializer.data)
  


#     def put(self,request,pk):
#         s1 = self.get_sub_by_pk(pk)
#         serializer =StudentSerializer(s1, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#     def delete(self,request,pk):
#         s1 = self.get_sub_by_pk(pk)
#         s1.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT) 


# class TeacherList(APIView):
#     def get(self, request):
#         sub = Teacher.objects.all()
#         serializer = TeacherSerializer(sub, many=True)
#         return Response(serializer.data)

# class TeacherCeate(APIView):
#     def post(self,request):
#         serializer = TeacherSerializer(data=request.data)
#         print(serializer)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             print('invalid')
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


# class TeacherDetail(APIView):
#     def get_sub_by_pk(self,pk):
#         try:
#             return Teacher.objects.get(pk=pk)

#         except:
#             return Response({
#                 'error': "Teacher does not exist"
#             }, status=status.HTTP_404_NOT_FOUND)


#     def get(self,request,pk):
#         s1 = self.get_sub_by_pk(pk)
#         serializer =TeacherSerializer(s1)
#         print(serializer)
#         return Response(serializer.data)
  


#     def put(self,request,pk):
#         s1 = self.get_sub_by_pk(pk)
#         serializer =TeacherSerializer(s1, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#     def delete(self,request,pk):
#         s1 = self.get_sub_by_pk(pk)
#         s1.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class RegisterStudent(APIView):
    def post(self,request):
        print(request.data)
        serializer = UserSerializer(data={'username': request.data["username"],"first_name":request.data["first_name"],'last_name':request.data["last_name"],'email':request.data['email'],"mobile_no":request.data["mobile_no"]
        ,'address':request.data['address'], "password":request.data['password']})
        print(serializer)
        if serializer.is_valid():
            user = serializer.save()
            student_obj = StudentSerializer(data = {"user":user.id ,"reqister_number":request.data["reqister_number"] , "college_name":request.data['college_name'] })

            if student_obj.is_valid():
                student_obj.save()
            else:
                return Response(student_obj.errors, status=status.HTTP_400_BAD_REQUEST)   
            return Response(student_obj.data,status=200)
        else:
            print('invalid')
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
