from rest_framework import serializers
from ..models import Student, User,Parents
from ..serializer import *

# Talaba serializeri - talabalar ma'lumotlarini JSON formatiga o'tkazish uchun
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'user', 'group', 'descreptions']

# Talaba foydalanuvchi serializeri - talabaning foydalanuvchi hisobi ma'lumotlarini JSON formatiga o'tkazish uchun
class StudentUserSerializer(serializers.ModelSerializer):
    # Foydalanuvchi faol yoki faol emasligi
    is_active = serializers.BooleanField(read_only=True)
    # Foydalanuvchi xodim yoki xodim emasligi
    is_staff = serializers.BooleanField(read_only=True)
    # Foydalanuvchi o'qituvchi yoki o'qituvchi emasligi
    is_teacher = serializers.BooleanField(read_only=True)
    # Foydalanuvchi talaba yoki talaba emasligi
    is_student = serializers.BooleanField(read_only=True)
    # Foydalanuvchi admin yoki admin emasligi
    is_admin = serializers.BooleanField(read_only=True)

    class Meta:
        model = User
        fields = (
            'id', 'phone_number', 'password', 'email', 'is_active', 'is_staff', 'is_admin', 'is_teacher', 'is_student',)

# Talaba yaratish serializeri - yangi talaba yaratish uchun
class StudentPostSerializer(serializers.Serializer):
    user = StudentUserSerializer()
    student = StudentSerializer()

# Ota-ona serializeri - ota-onalar ma'lumotlarini JSON formatiga o'tkazish uchun
class ParentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parents
        fields = ['id', 'student', 'full_name', 'phone_number', 'address', 'descriptions']