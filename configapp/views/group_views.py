from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets,status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ..models import GroupStudent,Table,TableType,Rooms,Subject
from ..serializer import GroupStudentSerializer,TableSerializer,TableTypeSerializer,RoomsSerializer,SubjectSerializer
from ..permissions import *
from ..pagination import *

# Guruh ViewSet - guruhlar bilan ishlash uchun
class GroupViewSet(viewsets.ModelViewSet):
    queryset = GroupStudent.objects.all()
    serializer_class = GroupStudentSerializer
    # permission_classes = [IsAuthenticated,IsAdminOrReadPatchOnly]

# Jadval ViewSet - dars jadvallari bilan ishlash uchun
class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    # permission_classes = [IsAuthenticated,IsAdminOrReadPatchOnly]

# Jadval turi ViewSet - jadval turlari bilan ishlash uchun
class TableTypeViewSet(viewsets.ModelViewSet):
    queryset = TableType.objects.all()
    serializer_class = TableTypeSerializer
    # permission_classes = [IsAuthenticated,IsAdminOrReadPatchOnly]

# Xona ViewSet - xonalar bilan ishlash uchun
class RoomsViewSet(viewsets.ModelViewSet):
    queryset = Rooms.objects.all()
    serializer_class = RoomsSerializer
    # permission_classes = [IsAuthenticated,IsAdminOrReadPatchOnly]

# Fan ViewSet - fanlar bilan ishlash uchun
class SubjectViewSet(viewsets.ViewSet):
    # permission_classes = [AdminUser]

    # Barcha fanlarni olish
    def list(self, request):
        subjects = Subject.objects.all()
        paginator = TeacherPagination()
        result_page = paginator.paginate_queryset(subjects, request)
        serializer = SubjectSerializer(result_page, many=True)
        return Response(serializer.data)

    # ID bo'yicha fanni olish
    def retrieve(self, request, pk=None):
        subject = get_object_or_404(Subject, pk=pk)
        serializer = SubjectSerializer(subject)
        return Response(serializer.data)

    # Yangi fan yaratish
    @action(detail=False, methods=['post'], url_path='create/subject')
    @swagger_auto_schema(request_body=SubjectSerializer)
    def create_subject(self, request):
        serializer = SubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Mavjud fanni yangilash
    @action(detail=True, methods=['put'], url_path='update/subject')
    @swagger_auto_schema(request_body=SubjectSerializer)
    def update_subject(self, request, pk=None):
        subject = get_object_or_404(Subject, pk=pk)
        serializer = SubjectSerializer(subject, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Fanni o'chirish
    @action(detail=True, methods=['delete'], url_path='delete/subject')
    def delete_subject(self, request, pk=None):
        subject = get_object_or_404(Subject, pk=pk)
        subject.delete()
        return Response({'status':True,'detail': 'Subject muaffaqiyatli uchirildi'}, status=status.HTTP_204_NO_CONTENT)
