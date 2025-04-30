from rest_framework import serializers

from ..models import *

# Oy ma'lumotlarini serializatsiya qilish uchun serializer
class MonthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Month
        fields = '__all__'

# To'lov ma'lumotlarini serializatsiya qilish uchun serializer
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

# To'lov turi ma'lumotlarini serializatsiya qilish uchun serializer
class PaymentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentType
        fields = '__all__'