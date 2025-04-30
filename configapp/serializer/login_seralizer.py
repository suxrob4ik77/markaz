from django.contrib.auth import authenticate
from rest_framework import serializers
from ..models import *

# Foydalanuvchi ma'lumotlarini serializatsiya qilish uchun serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'phone_number', 'password', 'email', 'is_active', 'is_staff', 'is_admin', 'is_teacher', 'is_student')

# O'qituvchi ma'lumotlarini serializatsiya qilish uchun serializer
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'user', 'departments', 'course', 'descriptions']

# Parolni o'zgartirish uchun serializer
class ChangePasswordSerializer(serializers.Serializer):
    # Eski parol
    old_password = serializers.CharField(required=True, write_only=True)
    # Yangi parol
    new_password = serializers.CharField(required=True, write_only=True)
    # Yangi parolni qayta kiritish
    re_new_password = serializers.CharField(required=True, write_only=True)

    def update(self, instance, validated_data):
        instance.password = validated_data.get('password', instance.password)
        if not validated_data['old_password']:
            raise serializers.ValidationError({'old_password': 'not found'})
        if not validated_data['new_password']:
            raise serializers.ValidationError({'new_password': 'not found'})

# SMS tasdiqlash uchun serializer
class VerifySMSSerializer(serializers.Serializer):
    # Telefon raqam
    phone_number = serializers.CharField()
    # Tasdiqlash kodi
    verification_code = serializers.CharField()

# SMS yuborish uchun serializer
class SMSSerializer(serializers.Serializer):
    # Telefon raqam
    phone_number = serializers.CharField()

# Tizimga kirish uchun serializer
class LoginSerializer(serializers.Serializer):
    # Telefon raqam (username o'rniga)
    phone_number = serializers.CharField()
    # Parol
    password = serializers.CharField()

    def validate(self, attrs):
        phone_number = attrs.get("phone_number")
        password = attrs.get("password")

        try:
            user = User.objects.get(phone_number=phone_number)
        except User.DoesNotExist:
            raise serializers.ValidationError({
                "success": False,
                "message": "User does not exist"
            })

        auth_user = authenticate(phone_number=phone_number, password=password)
        if auth_user is None:
            raise serializers.ValidationError({
                "success": False,
                "message": "Phone or password is invalid"
            })

        attrs['user'] = auth_user
        return attrs
