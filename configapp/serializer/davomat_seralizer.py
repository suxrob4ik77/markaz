from rest_framework import serializers
from ..models import *
from ..models.davomat_model import Davomat,Status

# Davomat holatlarini serializatsiya qilish uchun serializer
class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'

# Davomat ma'lumotlarini serializatsiya qilish uchun serializer
class DavomatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Davomat
        fields = '__all__'