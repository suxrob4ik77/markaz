from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from ..models import *
from ..serializer import StatusSerializer, DavomatSerializer
from ..pagination import StudentPagination
from ..permissions import *


class StatusViewSet(viewsets.ViewSet):
    # permission_classes = [AdminUser]

    def list(self, request):
        statuses = Status.objects.all()
        paginator = StudentPagination()
        result_page = paginator.paginate_queryset(statuses, request)
        serializer = StatusSerializer(result_page, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        status = get_object_or_404(Status, pk=pk)
        serializer = StatusSerializer(status)
        return Response(serializer.data)

    @action(detail=False, methods=['post'], url_path='create/status')
    @swagger_auto_schema(request_body=StatusSerializer)
    def create_status(self, request):
        serializer = StatusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['put'], url_path='update/status')
    @swagger_auto_schema(request_body=StatusSerializer)
    def update_status(self, request, pk=None):
        status = get_object_or_404(Status, pk=pk)
        serializer = StatusSerializer(status, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['delete'], url_path='delete/status')
    def delete_status(self, request, pk=None):
        status = get_object_or_404(Status, pk=pk)
        status.delete()
        return Response({'status':True,'detail': 'Status muaffaqiyatli uchirildi'}, status=status.HTTP_204_NO_CONTENT)

class DavomatViewSet(viewsets.ViewSet):
    # permission_classes = [AdminOrTeacher]

    def list(self, request):
        attendances = Davomat.objects.all()
        paginator = StudentPagination()
        result_page = paginator.paginate_queryset(attendances, request)
        serializer = DavomatSerializer(result_page, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        attendance = get_object_or_404(Davomat, pk=pk)
        serializer = DavomatSerializer(attendance)
        return Response(serializer.data)

    @action(detail=False, methods=['post'], url_path='create/attendance')
    @swagger_auto_schema(request_body=DavomatSerializer)
    def create_attendance(self, request):
        serializer = DavomatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['put'], url_path='update/attendance')
    @swagger_auto_schema(request_body=DavomatSerializer)
    def update_attendance(self, request, pk=None):
        attendance = get_object_or_404(Davomat, pk=pk)
        serializer = DavomatSerializer(attendance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['delete'], url_path='delete/attendance')
    def delete_attendance(self, request, pk=None):
        attendance = get_object_or_404(Davomat, pk=pk)
        attendance.delete()
        return Response({'status':True,'detail': 'Attendance muaffaqiyatli uchirildi'}, status=status.HTTP_204_NO_CONTENT)

