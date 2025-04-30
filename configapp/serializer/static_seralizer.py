from rest_framework.fields import DateField
from rest_framework.serializers import Serializer

# Sana filtri uchun serializer - ma'lum bir vaqt oralig'idagi ma'lumotlarni olish uchun
class DateFilterSerializer(Serializer):
    # Boshlanish sanasi
    start_date = DateField(required=True)
    # Tugash sanasi
    end_date = DateField(required=True)