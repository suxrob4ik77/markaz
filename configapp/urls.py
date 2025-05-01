# # Django REST framework va boshqa kerakli kutubxonalarni import qilish
# from rest_framework.routers import DefaultRouter
# from django.urls import path, include
# from rest_framework_simplejwt.views import TokenRefreshView, TokenBlacklistView
#
# # ViewSet va APIView klasslarini import qilish
# from .views import *
# from .views.davomat_views import *
# from .views.group_views import *
# from .views.static_views import StaticViewSet
#
# # DefaultRouter yaratish - API endpointlarini avtomatik yaratish uchun
# router = DefaultRouter()
#
# # O'qituvchilar uchun endpointlar
# router.register(r'teacher', TeacherViewSet, basename='teacher')
# # Talabalar uchun endpointlar
# router.register(r'student', StudentApi, basename='student')
# # Guruhlar uchun endpointlar
# router.register(r'group', GroupViewSet, basename='group')
# # Davomat holatlari uchun endpointlar
# router.register(r'status', StatusViewSet, basename='status')
# # Davomat uchun endpointlar
# router.register('davomat', DavomatViewSet, basename='davomat')
# # Ota-onalar uchun endpointlar
# router.register(r'parents', ParentViewSet, basename='parent')
# # Kafedralar uchun endpointlar
# router.register(r'department', DepartmentViewSet, basename='department')
# # Kurslar uchun endpointlar
# router.register(r'course', CourseViewSet, basename='course')
# # Jadval uchun endpointlar
# router.register(r'table', TableViewSet, basename='table')
# # Jadval turlari uchun endpointlar
# router.register(r'table_type', TableTypeViewSet, basename='tabletype')
# # Xonalar uchun endpointlar
# router.register(r'rooms', RoomsViewSet, basename='rooms')
# # Vazifalar uchun endpointlar
# router.register(r'homeworks',HomeworkViewSet,basename='homework')
# # Vazifa topshiriqlari uchun endpointlar
# router.register(r'homework-submissions',HomeworkSubmissionViewSet,basename='homework-submission')
# # Vazifa baholash uchun endpointlar
# router.register(r'homework-reviews',HomeworkReviewViewSet,basename='homework-review')
# # Oylar uchun endpointlar
# router.register(r'months',MonthViewSet,basename='month')
# # To'lov turlari uchun endpointlar
# router.register(r'payment-type',PaymentTypeViewSet,basename='payment-type')
# # To'lovlar uchun endpointlar
# router.register(r'payment',PaymentViewSet,basename='payment')
# # Fanlar uchun endpointlar
# router.register(r'subjects', SubjectViewSet, basename='subject')
# # Statistik ma'lumotlar uchun endpointlar
# router.register(r'static', StaticViewSet, basename='static')
#
# # Asosiy URL konfiguratsiyasi
# urlpatterns = [
#     # SMS yuborish uchun endpoint
#     path('post_send_otp/', PhoneSendOTP.as_view()),
#     # SMS tasdiqlash uchun endpoint
#     path('post_v_otp/', VerifySMS.as_view()),
#     # Ro'yxatdan o'tish uchun endpoint
#     path('register/', RegisterUserApi.as_view()),
#     # Token olish uchun endpoint
#     path('token/', LoginApi.as_view(), name='token'),
#     # Token yangilash uchun endpoint
#     path('tokenref', TokenRefreshView.as_view(), name='token'),
#     # Token bekor qilish uchun endpoint
#     path('tokenac', TokenBlacklistView.as_view(), name='token'),
#     # Router orqali yaratilgan barcha endpointlar
#     path('', include(router.urls)),
#     # Foydalanuvchi yaratish uchun endpoint
#     path('users/create/', RegisterUserApi.as_view()),
#     # Foydalanuvchi ma'lumotlarini ko'rish va o'zgartirish uchun endpoint
#     path('users/detail/<int:pk>/', UserDetailView.as_view(), name='users_detail'),
#     # Talabalar statistikasi uchun endpoint
#     path('students-statistic/', StudentFilterView.as_view(), name='recent-students'),
#     # O'qituvchilar statistikasi uchun endpoint
#     path('teachers-statistic/', TeacherFilterView.as_view(), name='teachers-statistic'),
#     # Davomat statistikasi uchun endpoint
#     path('davomat-statistics', DavomatFilterView.as_view(), name='davomat-statistics'),
#     # To'lovlar statistikasi uchun endpoint
#     path('payments-statistics', PaymentFilterView.as_view(), name='payments-statistics'),
#
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView, TokenBlacklistView

# ViewSet va APIView klasslarini import qilish
from .views import *
from .views.davomat_views import *
from .views.group_views import *
from .views.static_views import StaticViewSet

from django.urls import path,include


# DefaultRouter yaratish - API endpointlarini avtomatik yaratish uchun
router = DefaultRouter()

# O'qituvchilar uchun endpointlar
router.register(r'teacher', TeacherViewSet, basename='teacher')
# Talabalar uchun endpointlar
router.register(r'student', StudentApi, basename='student')
# Guruhlar uchun endpointlar
router.register(r'group', GroupViewSet, basename='group')
# Davomat holatlari uchun endpointlar
router.register(r'status', StatusViewSet, basename='status')
# Davomat uchun endpointlar
router.register('davomat', DavomatViewSet, basename='davomat')
# Ota-onalar uchun endpointlar
router.register(r'parents', ParentViewSet, basename='parent')
# Kafedralar uchun endpointlar
router.register(r'department', DepartmentViewSet, basename='department')
# Kurslar uchun endpointlar
router.register(r'course', CourseViewSet, basename='course')
# Jadval uchun endpointlar
router.register(r'table', TableViewSet, basename='table')
# Jadval turlari uchun endpointlar
router.register(r'table_type', TableTypeViewSet, basename='tabletype')
# Xonalar uchun endpointlar
router.register(r'rooms', RoomsViewSet, basename='rooms')
# Vazifalar uchun endpointlar
router.register(r'homeworks',HomeworkViewSet,basename='homework')
# Vazifa topshiriqlari uchun endpointlar
router.register(r'homework-submissions',HomeworkSubmissionViewSet,basename='homework-submission')
# Vazifa baholash uchun endpointlar
router.register(r'homework-reviews',HomeworkReviewViewSet,basename='homework-review')
# Oylar uchun endpointlar
router.register(r'months',MonthViewSet,basename='month')
# To'lov turlari uchun endpointlar
router.register(r'payment-type',PaymentTypeViewSet,basename='payment-type')
# To'lovlar uchun endpointlar
router.register(r'payment',PaymentViewSet,basename='payment')
# Fanlar uchun endpointlar
router.register(r'subjects', SubjectViewSet, basename='subject')
# Statistik ma'lumotlar uchun endpointlar
router.register(r'static', StaticViewSet, basename='static')

# Asosiy URL konfiguratsiyasi
urlpatterns = [
    # SMS yuborish uchun endpoint
    path('post_send_otp/', PhoneSendOTP.as_view()),
    # SMS tasdiqlash uchun endpoint
    path('post_v_otp/', VerifySMS.as_view()),
    # Ro'yxatdan o'tish uchun endpoint
    path('register/', RegisterUserApi.as_view()),
    # Token olish uchun endpoint
    path('token/', LoginApi.as_view(), name='token'),
    # Token yangilash uchun endpoint
    path('tokenref', TokenRefreshView.as_view(), name='token'),
    # Token bekor qilish uchun endpoint
    path('tokenac', TokenBlacklistView.as_view(), name='token'),
    # Router orqali yaratilgan barcha endpointlar
    path('', include(router.urls)),
    # Foydalanuvchi yaratish uchun endpoint
    path('users/create/', RegisterUserApi.as_view()),
    # Foydalanuvchi ma'lumotlarini ko'rish va o'zgartirish uchun endpoint
    path('users/detail/<int:pk>/', UserDetailView.as_view(), name='users_detail'),
    # Talabalar statistikasi uchun endpoint
    path('students-statistic/', StudentFilterView.as_view(), name='recent-students'),
    # O'qituvchilar statistikasi uchun endpoint
    path('teachers-statistic/', TeacherFilterView.as_view(), name='teachers-statistic'),
    # Davomat statistikasi uchun endpoint
    path('davomat-statistics', DavomatFilterView.as_view(), name='davomat-statistics'),
    # To'lovlar statistikasi uchun endpoint
    path('payments-statistics', PaymentFilterView.as_view(), name='payments-statistics'),
]