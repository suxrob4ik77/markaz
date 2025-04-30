from rest_framework.pagination import PageNumberPagination

# Talabalar ro'yxati uchun sahifalash
class StudentPagination(PageNumberPagination):
    page_size = 2
    page_query_param = 'page'
    page_size_query_param = 'page_size'
    max_page_size = 100

# O'qituvchilar ro'yxati uchun sahifalash
class TeacherPagination(PageNumberPagination):
    page_size = 2
    page_query_param = 'page'
    page_size_query_param = 'page_size'
    max_page_size = 100

# Ota-onalar ro'yxati uchun sahifalash
class ParentsPagination(PageNumberPagination):
    page_size = 2
    page_query_param = 'page'
    page_size_query_param = 'page_size'
    max_page_size = 100

# Kurslar ro'yxati uchun sahifalash
class CoursePagination(PageNumberPagination):
    page_size = 2
    page_query_param = 'page'
    page_size_query_param = 'page_size'
    max_page_size = 100

# Kafedralar ro'yxati uchun sahifalash
class DepartmentPagination(PageNumberPagination):
    page_size = 2
    page_query_param = 'page'
    page_size_query_param = 'page_size'
    max_page_size = 100

# Oylar ro'yxati uchun sahifalash
class MonthPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 50

# To'lovlar ro'yxati uchun sahifalash
class PaynetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 50

# To'lov turlari ro'yxati uchun sahifalash
class PaynettypePagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 50


