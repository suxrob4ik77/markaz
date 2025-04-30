from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from ..models import *
from ..permissions import *
from ..pagination import *
from ..serializer import *

# Uy vazifalari bilan ishlash uchun ViewSet
class HomeworkViewSet(viewsets.ViewSet):
    # permission_classes = [AdminOrTeacher]

    # Barcha uy vazifalarini olish
    def list(self, request):
        homeworks = Homework.objects.all()
        serializer = HomeworkSerializer(homeworks, many=True)
        return Response(serializer.data)

    # ID bo'yicha uy vazifasini olish
    def retrieve(self, request, pk=None):
        homework = get_object_or_404(Homework, pk=pk)
        serializer = HomeworkSerializer(homework)
        return Response(serializer.data)

    # Yangi uy vazifasi yaratish
    @action(detail=False, methods=['post'], url_path='create')
    @swagger_auto_schema(request_body=HomeworkSerializer)
    def create_homework(self, request):
        serializer = HomeworkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['teacher'] = request.user.teacher
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Mavjud uy vazifasini yangilash
    @action(detail=True, methods=['put'], url_path='update')
    @swagger_auto_schema(request_body=HomeworkSerializer)
    def update_homework(self, request, pk=None):
        homework = get_object_or_404(TableType, pk=pk)
        serializer = TableTypeSerializer(homework, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Uy vazifasini o'chirish
    @action(detail=True, methods=['delete'], url_path='delete')
    def delete_homework(self, request, pk=None):
        homework = get_object_or_404(Homework, pk=pk)
        homework.delete()
        return Response({'status':True,'detail': 'Homework muaffaqiyatli uchirildi'}, status=status.HTTP_204_NO_CONTENT)


# Uy vazifalarini baholash bilan ishlash uchun ViewSet
class HomeworkReviewViewSet(viewsets.ViewSet):
    # permission_classes = [AdminOrTeacher]

    # Barcha uy vazifasi baholarini olish
    def list(self, request):
        homework = HomeworkReview.objects.all()
        serializer = HomeworkReviewSerializer(homework, many=True)
        return Response(serializer.data)

    # ID bo'yicha uy vazifasi bahosini olish
    def retrieve(self, request, pk=None):
        homework = get_object_or_404(HomeworkReview, pk=pk)
        serializer = HomeworkReviewSerializer(homework)
        return Response(serializer.data)

    # Yangi uy vazifasi bahosi yaratish
    @action(detail=False, methods=['post'], url_path='create/review')
    @swagger_auto_schema(request_body=HomeworkReviewSerializer)
    def create_homework_review(self, request):
        serializer = HomeworkReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['teacher'] = request.user.teacher
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Mavjud uy vazifasi bahosini yangilash
    @action(detail=True, methods=['put'], url_path='update/review')
    @swagger_auto_schema(request_body=HomeworkReviewSerializer)
    def update_homework_review(self, request, pk=None):
        homework = get_object_or_404(HomeworkReviewSerializer, pk=pk)
        serializer = HomeworkReviewSerializer(homework, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Uy vazifasi bahosini o'chirish
    @action(detail=True, methods=['delete'], url_path='delete/review')
    def delete_homework_review(self, request, pk=None):
        homework = get_object_or_404(HomeworkReviewSerializer, pk=pk)
        homework.delete()
        return Response({'status':True,'detail': 'HomeworkReview muaffaqiyatli uchirildi'}, status=status.HTTP_204_NO_CONTENT)


# Uy vazifalarini topshirish bilan ishlash uchun ViewSet
class HomeworkSubmissionViewSet(viewsets.ViewSet):
    # permission_classes = [AdminOrStudent]

    # Barcha topshirilgan uy vazifalarini olish
    def list(self, request):
        homework = HomeworkSubmission.objects.all()
        serializer = HomeworkSubmissionSerializer(homework, many=True)
        return Response(serializer.data)

    # ID bo'yicha topshirilgan uy vazifasini olish
    def retrieve(self, request, pk=None):
        homework = get_object_or_404(HomeworkSubmission, pk=pk)
        serializer = HomeworkSubmissionSerializer(homework)
        return Response(serializer.data)

    # Yangi uy vazifasi topshirish yaratish
    @action(detail=False, methods=['post'], url_path='create/submission')
    @swagger_auto_schema(request_body=HomeworkSubmissionSerializer)
    def create_homework_submission(self, request):
        serializer = HomeworkSubmissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['student'] = request.user.student
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Mavjud uy vazifasi topshirishni yangilash
    @action(detail=True, methods=['put'], url_path='update/submission')
    @swagger_auto_schema(request_body=HomeworkSubmissionSerializer)
    def update_homework_submission(self, request, pk=None):
        homework = get_object_or_404(HomeworkSubmission, pk=pk)
        serializer = HomeworkSubmissionSerializer(homework, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Uy vazifasi topshirishni o'chirish
    @action(detail=True, methods=['delete'], url_path='delete/submission')
    def delete_homework_submission(self, request, pk=None):
        homework = get_object_or_404(HomeworkSubmission, pk=pk)
        homework.delete()
        return Response({'status':True,'detail': 'HomeworkSubmission muaffaqiyatli uchirildi'}, status=status.HTTP_204_NO_CONTENT)