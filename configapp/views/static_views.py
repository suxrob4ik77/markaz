from datetime import datetime

from django.db.models import Count, Q, Sum
from django.utils.timezone import make_aware
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from ..models import *
from ..serializer import *
from .davomat_views import *


class StudentFilterView(APIView):
    # permission_classes = [IsAdminUser]

    @swagger_auto_schema(request_body=DateFilterSerializer)
    def post(self, request):
        serializer = DateFilterSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        start_date = serializer.validated_data['start_date']
        end_date = serializer.validated_data['end_date']

        start_date = make_aware(datetime.combine(start_date, datetime.min.time()))
        end_date = make_aware(datetime.combine(end_date, datetime.max.time()))

        total_students = Student.objects.count()
        graduated_students = Student.objects.filter(
            group__is_active=False, created_at__range=[start_date, end_date]
        ).count()
        studying_students = Student.objects.filter(
            group__is_active=True, created_at__range=[start_date, end_date]
        ).count()
        registered_students = Student.objects.filter(
            created_at__range=[start_date, end_date]
        ).count()

        return Response({
            "total_students": total_students,
            "registered_students": registered_students,
            "studying_students": studying_students,
            "graduated_students": graduated_students,
        }, status=status.HTTP_200_OK)


class TeacherFilterView(APIView):
    # permission_classes = [IsAdminUser]

    @swagger_auto_schema(request_body=DateFilterSerializer)
    def post(self, request):
        serializer = DateFilterSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        start_date = serializer.validated_data['start_date']
        end_date = serializer.validated_data['end_date']

        start_date = make_aware(datetime.combine(start_date, datetime.min.time()))
        end_date = make_aware(datetime.combine(end_date, datetime.max.time()))

        total_teachers = Teacher.objects.count()
        registered_teachers = Teacher.objects.filter(
            created_at__range=[start_date, end_date]
        ).count()

        top_teachers = (
            Student.objects.filter(
                created_at__range=[start_date, end_date]
            )
            .values("group__teacher__user__phone_number")
            .annotate(total_students=Count("id"))
            .order_by("-total_students")[:10]
        )

        return Response({
            "total_teachers": total_teachers,
            "registered_teachers": registered_teachers,
            "top_teachers": top_teachers,
        }, status=status.HTTP_200_OK)


class CourseFilterView(APIView):
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(request_body=DateFilterSerializer)
    def post(self, request):
        serializer = DateFilterSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        start_date = serializer.validated_data['start_date']
        end_date = serializer.validated_data['end_date']

        start_date = make_aware(datetime.combine(start_date, datetime.min.time()))
        end_date = make_aware(datetime.combine(end_date, datetime.max.time()))

        courses_statistics = (
            Course.objects.annotate(
                total_registered_students=Count(
                    "c_student",
                    filter=Q(c_student__created_at__range=[start_date, end_date])
                ),
                total_studying_students=Count(
                    "c_student",
                    filter=Q(c_student__group__active=True, c_student__created_at__range=[start_date, end_date])
                ),
                total_graduated_students=Count(
                    "c_student",
                    filter=Q(c_student__group__active=False, c_student__created_at__range=[start_date, end_date])
                ),
            ).values("title", "total_registered_students", "total_studying_students", "total_graduated_students")
        )

        return Response(courses_statistics, status=status.HTTP_200_OK)

class DavomatFilterView(APIView):
    # permission_classes = [IsAdminUser]

    @swagger_auto_schema(request_body=DateFilterSerializer)
    def post(self, request):
        serializer = DateFilterSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        start_date = serializer.validated_data['start_date']
        end_date = serializer.validated_data['end_date']

        start_date = make_aware(datetime.combine(start_date, datetime.min.time()))
        end_date = make_aware(datetime.combine(end_date, datetime.max.time()))

        attendance_stats = (
            Davomat.objects.filter(
                created_at__range=[start_date, end_date]
            ).aggregate(
                total_present=Count("id", filter=Q(status__title="Present")),
                total_absent=Count("id", filter=Q(status__title="Absent")),
                total_late=Count("id", filter=Q(status__title="Late")),
                total_excused=Count("id", filter=Q(status__title="Excused"))
            )
        )

        return Response(attendance_stats, status=status.HTTP_200_OK)

# class DavomatFilterView(APIView):
#     # permission_classes = [IsAdminUser]
#
#     @swagger_auto_schema(request_body=DateFilterSerializer)
#     def post(self, request):
#         serializer = DateFilterSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#         start_date = serializer.validated_data['start_date']
#         end_date = serializer.validated_data['end_date']
#
#         start_date = make_aware(datetime.combine(start_date, datetime.min.time()))
#         end_date = make_aware(datetime.combine(end_date, datetime.max.time()))
#
#         attendance_stats = (
#             Davomat.objects.filter(
#                 created_at__range=[start_date, end_date]
#             ).aggregate(
#                 total_present=Count("id", filter=Q(is_status=1)),
#                 total_absent=Count("id", filter=Q(is_status=2)),
#                 total_late=Count("id", filter=Q(is_status=3)),
#                 total_excused=Count("id", filter=Q(is_status=4)),
#             )
#         )
#
#         return Response(attendance_stats, status=status.HTTP_200_OK)
#

class PaymentFilterView(APIView):
    # permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=DateFilterSerializer)
    def post(self, request):
        serializer = DateFilterSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        start_date = serializer.validated_data['start_date']
        end_date = serializer.validated_data['end_date']

        start_date = make_aware(datetime.combine(start_date, datetime.min.time()))
        end_date = make_aware(datetime.combine(end_date, datetime.max.time()))

        payment_stats = (
            Payment.objects.filter(
                created_at__range=[start_date, end_date]
            ).aggregate(
                total_amount=Sum("price"),
                total_students=Count("student", distinct=True)
            )
        )

        return Response(payment_stats, status=status.HTTP_200_OK)
