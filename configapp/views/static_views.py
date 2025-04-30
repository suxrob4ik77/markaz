from datetime import datetime

from django.db.models import Count, Q, Sum, F
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

        # start_date va end_date ni timezone aware qilish
        start_date = make_aware(datetime.combine(start_date, datetime.min.time()))
        end_date = make_aware(datetime.combine(end_date, datetime.max.time()))

        # Statistika
        total_students = Student.objects.count()

        registered_students = Student.objects.filter(
            created_at__range=[start_date, end_date]
        ).count()

        # ManyToManyField bo'lgan group uchun to'g'ri filterlash
        graduated_students = Student.objects.filter(
            group__in=GroupStudent.objects.filter(is_active=False),
            created_at__range=[start_date, end_date]
        ).distinct().count()

        studying_students = Student.objects.filter(
            group__in=GroupStudent.objects.filter(is_active=True),
            created_at__range=[start_date, end_date]
        ).distinct().count()

        return Response({
            "total_students": total_students,
            "registered_students": registered_students,
            "studying_students": studying_students,
            "graduated_students": graduated_students,
        }, status=status.HTTP_200_OK)
# class StudentFilterView(APIView):
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
#         total_students = Student.objects.count()
#         graduated_students = Student.objects.filter(
#             group__is_active=False, created_at__range=[start_date, end_date]
#         ).count()
#         studying_students = Student.objects.filter(
#             group__is_active=True, created_at__range=[start_date, end_date]
#         ).count()
#         registered_students = Student.objects.filter(
#             created_at__range=[start_date, end_date]
#         ).count()
#
#         return Response({
#             "total_students": total_students,
#             "registered_students": registered_students,
#             "studying_students": studying_students,
#             "graduated_students": graduated_students,
#         }, status=status.HTTP_200_OK)
#

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

from django.db.models import Count, Q
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Course
from ..serializer import DateFilterSerializer  # Sizning serializer importi

from django.db.models import Count, Q
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Course
from ..serializer import DateFilterSerializer  # Sizning serializer importi

# class CourseFilterView(APIView):
#     permission_classes = [IsAdminUser]
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
#         courses_statistics = (
#             Course.objects.annotate(
#                 total_registered_students=Count(
#                     "groupstudent__student",  # groupstudent orqali Student ga kirish
#                     filter=Q(groupstudent__student__created_at__range=[start_date, end_date])
#                 ),
#                 total_studying_students=Count(
#                     "groupstudent__student",
#                     filter=Q(groupstudent__student__group__is_active=True,
#                              groupstudent__student__created_at__range=[start_date, end_date])
#                 ),
#                 total_graduated_students=Count(
#                     "groupstudent__student",
#                     filter=Q(groupstudent__student__group__is_active=False,
#                              groupstudent__student__created_at__range=[start_date, end_date])
#                 ),
#             ).values("title", "total_registered_students", "total_studying_students", "total_graduated_students")
#         )
#
#         return Response(courses_statistics, status=status.HTTP_200_OK)

# class CourseFilterView(APIView):
#     permission_classes = [IsAdminUser]
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
#         courses_statistics = (
#             Course.objects.annotate(
#                 total_registered_students=Count(
#                     "c_student",
#                     filter=Q(c_student__created_at__range=[start_date, end_date])
#                 ),
#                 total_studying_students=Count(
#                     "c_student",
#                     filter=Q(c_student__group__active=True, c_student__created_at__range=[start_date, end_date])
#                 ),
#                 total_graduated_students=Count(
#                     "c_student",
#                     filter=Q(c_student__group__active=False, c_student__created_at__range=[start_date, end_date])
#                 ),
#             ).values("title", "total_registered_students", "total_studying_students", "total_graduated_students")
#         )
#
#         return Response(courses_statistics, status=status.HTTP_200_OK)

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

# Statistik ma'lumotlarni olish uchun viewset
class StaticViewSet(viewsets.ViewSet):
    # permission_classes = [IsAdminOnly]

    # Barcha statistik ma'lumotlarni olish
    def list(self, request):
        # Talabalar soni
        student_count = User.objects.filter(role='student').count()
        # O'qituvchilar soni
        teacher_count = User.objects.filter(role='teacher').count()
        # Guruhlar soni
        group_count = GroupStudent.objects.count()
        # To'lovlar summasi
        payment_sum = Payment.objects.aggregate(total=Sum('amount'))['total'] or 0

        data = {
            'student_count': student_count,
            'teacher_count': teacher_count,
            'group_count': group_count,
            'payment_sum': payment_sum
        }
        return Response(data)

    # Talabalar statistikasini olish
    @action(detail=False, methods=['get'], url_path='student-stats')
    def student_stats(self, request):
        # Talabalar soni guruhlar bo'yicha
        group_stats = GroupStudent.objects.annotate(
            student_count=Count('get_student')
        ).values('title', 'student_count')

        # Talabalar soni kurslar bo'yicha
        course_stats = Course.objects.annotate(
            student_count=Count('groupstudent__get_student')
        ).values('title', 'student_count')

        data = {
            'group_stats': group_stats,
            'course_stats': course_stats
        }
        return Response(data)

    # O'qituvchilar statistikasini olish
    @action(detail=False, methods=['get'], url_path='teacher-stats')
    def teacher_stats(self, request):
        # O'qituvchilar soni kurslar bo'yicha
        course_stats = Course.objects.annotate(
            teacher_count=Count('get_course')
        ).values('title', 'teacher_count')

        # O'qituvchilar soni guruhlar bo'yicha
        group_stats = GroupStudent.objects.annotate(
            teacher_count=Count('teacher')
        ).values('title', 'teacher_count')

        data = {
            'course_stats': course_stats,
            'group_stats': group_stats
        }
        return Response(data)

    # To'lovlar statistikasini olish
    @action(detail=False, methods=['get'], url_path='payment-stats')
    def payment_stats(self, request):
        # To'lovlar summasi oylar bo'yicha
        month_stats = Month.objects.annotate(
            payment_sum=Sum('payment__price')
        ).values('title', 'payment_sum')

        # To'lovlar summasi to'lov turlari bo'yicha
        type_stats = PaymentType.objects.annotate(
            payment_sum=Sum('payment__price')
        ).values('title', 'payment_sum')

        data = {
            'month_stats': month_stats,
            'type_stats': type_stats
        }
        return Response(data)

    # Davomat statistikasini olish
    @action(detail=False, methods=['get'], url_path='attendance-stats')
    def attendance_stats(self, request):
        # Davomat foizi guruhlar bo'yicha
        group_stats = GroupStudent.objects.annotate(
            total_lessons=Count('lessons'),
            attended_lessons=Count('lessons__attendances', filter=Q(lessons__attendances__status__name='Keldi')),
            attendance_percentage=F('attended_lessons') * 100 / F('total_lessons')
        ).values('name', 'attendance_percentage')

        # Davomat foizi talabalar bo'yicha
        student_stats = User.objects.filter(role='student').annotate(
            total_lessons=Count('attendances'),
            attended_lessons=Count('attendances', filter=Q(attendances__status__name='Keldi')),
            attendance_percentage=F('attended_lessons') * 100 / F('total_lessons')
        ).values('first_name', 'last_name', 'attendance_percentage')

        data = {
            'group_stats': group_stats,
            'student_stats': student_stats
        }
        return Response(data)

    # Vazifalar statistikasini olish
    @action(detail=False, methods=['get'], url_path='homework-stats')
    def homework_stats(self, request):
        # Vazifalar bajarilishi guruhlar bo'yicha
        group_stats = GroupStudent.objects.annotate(
            total_homeworks=Count('homeworks'),
            completed_homeworks=Count('homeworks__submissions', filter=Q(homeworks__submissions__is_checked=True)),
            completion_percentage=F('completed_homeworks') * 100 / F('total_homeworks')
        ).values('title', 'completion_percentage')

        # Vazifalar bajarilishi talabalar bo'yicha
        student_stats = User.objects.filter(is_student=True).annotate(
            total_homeworks=Count('student__submissions'),
            completed_homeworks=Count('student__submissions', filter=Q(student__submissions__is_checked=True)),
            completion_percentage=F('completed_homeworks') * 100 / F('total_homeworks')
        ).values('phone_number', 'completion_percentage')

        data = {
            'group_stats': group_stats,
            'student_stats': student_stats
        }
        return Response(data)

    # Ma'lum bir vaqt oralig'idagi statistikani olish
    @action(detail=False, methods=['post'], url_path='date-range-stats')
    @swagger_auto_schema(request_body=DateFilterSerializer)
    def date_range_stats(self, request):
        serializer = DateFilterSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        start_date = serializer.validated_data['start_date']
        end_date = serializer.validated_data['end_date']

        # To'lovlar summasi
        payment_sum = Payment.objects.filter(
            created_at__range=[start_date, end_date]
        ).aggregate(total=Sum('amount'))['total'] or 0

        # Davomat foizi
        attendance_stats = Davomat.objects.filter(
            created_at__range=[start_date, end_date]
        ).aggregate(
            total=Count('id'),
            attended=Count('id', filter=Q(status__name='Keldi')),
            percentage=F('attended') * 100 / F('total')
        )

        # Vazifalar bajarilishi
        homework_stats = Homework.objects.filter(
            created_at__range=[start_date, end_date]
        ).aggregate(
            total=Count('id'),
            completed=Count('id', filter=Q(is_completed=True)),
            percentage=F('completed') * 100 / F('total')
        )

        data = {
            'payment_sum': payment_sum,
            'attendance_stats': attendance_stats,
            'homework_stats': homework_stats
        }
        return Response(data)
