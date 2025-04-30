from rest_framework import serializers
from ..models import *
from ..serializer import *

# Uy vazifasi serializeri - uy vazifalarini JSON formatiga o'tkazish uchun
class HomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = '__all__'
        # O'qituvchi maydoni faqat o'qish uchun
        extra_kwargs = {'teacher': {'read_only': True}}

# Uy vazifasini topshirish serializeri - topshirilgan vazifalarni JSON formatiga o'tkazish uchun
class HomeworkSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeworkSubmission
        fields = '__all__'
        # Talaba va tekshirilganlik maydonlari faqat o'qish uchun
        extra_kwargs = {'student': {'read_only': True},
                        'is_checked': {'read_only': True}}

# Uy vazifasini baholash serializeri - baholarni JSON formatiga o'tkazish uchun
class HomeworkReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeworkReview
        fields = '__all__'
        # O'qituvchi maydoni faqat o'qish uchun
        extra_kwargs = {
            'teacher': {'read_only': True}
        }