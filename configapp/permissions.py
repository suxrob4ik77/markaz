from rest_framework.permissions import BasePermission

class TeacherPermission(BasePermission):
    """
        Teacher: faqat GET va PATCH qilishga ruxsat
        Admin: to'liq CRUD
    """
    def has_permission(self, request, view):
        if request.user.is_admin:
            return True

        if request.user.is_teacher and request.method in ['GET', 'POST']:
            return True

        return False

# from rest_framework.permissions import BasePermission
#
# class AdminUser(BasePermission):
#     def has_permission(self, request, view):
#         if not request.user.is_authenticated:
#             return False
#         return request.user.is_authenticated and request.user.is_admin or request.user.is_staff
#
# class AdminOrTeacher(BasePermission):
#     def has_permission(self, request, view):
#         if not request.user.is_authenticated:
#             return False
#         return request.user.is_authenticated and request.user.is_teacher or request.user.is_staff or request.user.is_admin
#
# class AdminOrStudent(BasePermission):
#     def has_permission(self, request, view):
#         if not request.user.is_authenticated:
#             return False
#         return request.user.is_authenticated and request.user.is_student or request.user.is_staff or request.user.is_admin
#
# class AdminOrOwner(BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if not request.user.is_authenticated:
#             return False
#         return request.user.is_authenticated and obj.user == request.user or request.user.is_staff or request.user.is_admin
#
#
#