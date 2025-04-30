from rest_framework import serializers

from . import *
from ..models import *

# O'qituvchi serializeri - o'qituvchilar ma'lumotlarini JSON formatiga o'tkazish uchun
class TeacherSerializer(serializers.ModelSerializer):
    # user = models.CharField(read_only=True)

    class Meta:
        model = Teacher
        fields = ['id','user','departments','course','descriptions']



# O'qituvchi foydalanuvchi serializeri - o'qituvchining foydalanuvchi hisobi ma'lumotlarini JSON formatiga o'tkazish uchun
class TeacherUserSerializer(serializers.ModelSerializer):
    # Foydalanuvchi faol yoki faol emasligi
    is_active = serializers.BooleanField(read_only=True)
    # Foydalanuvchi xodim yoki xodim emasligi
    is_staff = serializers.BooleanField(read_only=True)
    # Foydalanuvchi admin yoki admin emasligi
    is_admin = serializers.BooleanField(read_only=True)
    # Foydalanuvchi o'qituvchi yoki o'qituvchi emasligi
    is_teacher = serializers.BooleanField(read_only=True)
    # Foydalanuvchi talaba yoki talaba emasligi
    is_student = serializers.BooleanField(read_only=True)


    class Meta:
        model = User
        fields = (
            'id', 'phone_number', 'password', 'email', 'is_active', 'is_staff', 'is_admin', 'is_teacher', 'is_student')



# O'qituvchi yaratish serializeri - yangi o'qituvchi yaratish uchun
class TeacherPostSerializer(serializers.Serializer):
    user = TeacherUserSerializer()
    teacher = TeacherSerializer()

# Kurs serializeri - kurslar ma'lumotlarini JSON formatiga o'tkazish uchun
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'descriptions']

# Bo'lim serializeri - bo'limlar ma'lumotlarini JSON formatiga o'tkazish uchun
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ['id', 'title', 'is_active', 'descriptions']


# from rest_framework import serializers
# from . import UserSerializer
# from ..models import *
#
# class CourseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Course
#         fields = ['id', 'title', 'descriptions']
#
# class DepartmentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Departments
#         fields = ['id', 'title', 'is_active', 'search_fields', 'descriptions']
#
# class TeacherSerializer(serializers.ModelSerializer):
#     user = serializers.PrimaryKeyRelatedField(read_only=True)
#     class Meta:
#         model = Teacher
#         fields = ['id', 'user', 'department', 'course', 'descriptions']
#
#
# class TeacherUserSerializer(serializers.ModelSerializer):
#     is_active = serializers.BooleanField(read_only=True)
#     is_teacher = serializers.BooleanField(read_only=True)
#     is_staff = serializers.BooleanField(read_only=True)
#     is_admin = serializers.BooleanField(read_only=True)
#     is_student = serializers.BooleanField(read_only=True)
#     class Meta:
#         model = User
#         fields = (
#             'id', 'phone_number', 'password', 'email', 'is_active', 'is_staff', 'is_admin', 'is_teacher', 'is_student')
#
# class TeacherPostSerializer(serializers.Serializer):
#     user = TeacherUserSerializer()
#     teacher = TeacherSerializer()