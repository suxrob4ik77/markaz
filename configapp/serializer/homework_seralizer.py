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
# class HomeworkSubmissionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = HomeworkSubmission
#         fields = '__all__'
#         # Talaba va tekshirilganlik maydonlari faqat o'qish uchun
#         extra_kwargs = {'student': {'read_only': True},
#                         'is_checked': {'read_only': True}}
#
# # Uy vazifasini baholash serializeri - baholarni JSON formatiga o'tkazish uchun
# class HomeworkReviewSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = HomeworkReview
#         fields = '__all__'
#         # O'qituvchi maydoni faqat o'qish uchun
#         extra_kwargs = {
#             'teacher': {'read_only': True}
#         }
class HomeworkSubmissionSerializer(serializers.ModelSerializer):
    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all(), required=True)  # student ID
    homework = serializers.PrimaryKeyRelatedField(queryset=Homework.objects.all(), required=True)

    class Meta:
        model = HomeworkSubmission
        fields = ['id', 'homework', 'student', 'link', 'is_checked', 'created_at', 'updated_at']
        read_only_fields = ['id', 'student', 'is_checked', 'created_at', 'updated_at']
        extra_kwargs = {
            'homework': {'required': True},
            'link': {
                'required': True,
                'max_length': 255,
                'help_text': 'Link to the homework submission'
            }
        }

    def validate_link(self, value):
        if not value.strip():
            raise serializers.ValidationError("Link cannot be empty or contain only whitespace")
        return value


class HomeworkReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeworkReview
        fields = ['id', 'submission', 'teacher', 'comment', 'ball', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
        extra_kwargs = {
            'submission': {'required': True},
            'comment': {
                'required': False,
                'allow_null': True,
                'help_text': 'Review comment'
            },
            'ball': {
                'required': False,
                'allow_null': True,
                'min_value': 0,
                'max_value': 100,
                'help_text': 'Grade from 0 to 100'
            }
        }

    def create(self, validated_data):
        # is_checked ni true qilish
        submission = validated_data['submission']
        submission.is_checked = True
        submission.save()

        return super().create(validated_data)