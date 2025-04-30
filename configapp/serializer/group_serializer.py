from rest_framework import serializers
from ..models import *
from .teacher_serializer import *

# Guruh serializeri - guruh ma'lumotlarini JSON formatiga o'tkazish uchun
class GroupStudentSerializer(serializers.ModelSerializer):
    # Guruhning o'qituvchilari ma'lumotlari
    teacher = TeacherSerializer(read_only=Teacher,many=True)

    class Meta:
        model = GroupStudent
        fields = '__all__'

# Jadval serializeri - dars jadvalini JSON formatiga o'tkazish uchun
class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ['id', 'start_time', 'end_time', 'room', 'type', 'descriptions']

# Jadval turi serializeri - jadval turlarini JSON formatiga o'tkazish uchun
class TableTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableType
        fields = ['id', 'title', 'descriptions']

# Xona serializeri - xonalar ma'lumotlarini JSON formatiga o'tkazish uchun
class RoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = ['id', 'title', 'descriptions']

# Fan serializeri - fanlar ma'lumotlarini JSON formatiga o'tkazish uchun
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


