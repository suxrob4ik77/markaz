# from django.db import models
# from .auth_users import *
# from .model_teacher import *
#
#
# class Homework(BaseModel):
#     title = models.CharField(max_length=255)
#     description = models.TextField(null=True, blank=True)
#     course = models.ForeignKey('app_courses.Course', on_delete=models.CASCADE, related_name='homeworks')
#     group = models.ForeignKey('app_courses.Group', on_delete=models.CASCADE, related_name='homeworks')
#     teacher = models.ForeignKey('app_users.Teacher', on_delete=models.CASCADE, related_name='homeworks')
#
#     def __str__(self):
#         return f"{self.title} - {self.group.title}"
#
#     class Meta:
#         verbose_name = 'Homework'
#         verbose_name_plural = 'Homeworks'
#
# class HomeworkSubmission(BaseModel):
#     homework = models.ForeignKey(Homework, on_delete=models.CASCADE, related_name='submissions')
#     student = models.ForeignKey('app_users.Student', on_delete=models.CASCADE, related_name='submissions')
#     link = models.CharField(max_length=255)
#     is_checked = models.BooleanField(default=False)
#
#     def __str__(self):
#         return f"{self.student.user.phone_number} - {self.homework.title}"
#
#     verbose_name = 'Homework Submission'
#     verbose_name_plural = 'Homework Submissions'
#
# class HomeworkReview(BaseModel):
#     submission = models.OneToOneField(HomeworkSubmission, on_delete=models.CASCADE, related_name='review')
#     teacher = models.ForeignKey('app_users.Teacher', on_delete=models.CASCADE, related_name='reviews')
#     comment = models.TextField(null=True, blank=True)
#     grade = models.PositiveIntegerField(null=True, blank=True)
#
#     def __str__(self):
#         return f"Review for {self.submission.student.user.phone_number} - {self.submission.homework.title}"


from django.db import models
from ..models import BaseModel, Course, GroupStudent, Teacher, Student

# Uy vazifasi modeli - o'qituvchi tomonidan guruhga beriladigan vazifalar
class Homework(BaseModel):
    # Uy vazifasining sarlavhasi
    title = models.CharField(max_length=255)
    # Uy vazifasining tavsifi
    description = models.TextField(null=True, blank=True)
    # Uy vazifasi berilgan guruh
    group = models.ForeignKey(GroupStudent, on_delete=models.CASCADE, related_name='homeworks')
    # Uy vazifasini bergan o'qituvchi
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='homeworks')

    def __str__(self):
        return f"{self.title} - {self.group.title}"

    class Meta:
        verbose_name = 'Uy vazifasi'
        verbose_name_plural = 'Uy vazifalari'

# Uy vazifasini topshirish modeli - talaba tomonidan topshirilgan vazifalar
class HomeworkSubmission(BaseModel):
    # Topshirilgan uy vazifasi
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE, related_name='submissions')
    # Vazifani topshirgan talaba
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='submissions')
    # Vazifaning havolasi yoki manzili
    link = models.CharField(max_length=255)
    # Vazifaning tekshirilganligi
    is_checked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.user.phone_number} - {self.homework.title}"

    class Meta:
        verbose_name = 'Uy vazifasini topshirish'
        verbose_name_plural = 'Uy vazifalarini topshirishlar'

# Uy vazifasini baholash modeli - o'qituvchi tomonidan berilgan baholar
class HomeworkReview(BaseModel):
    # Baholanayotgan topshirilgan vazifa
    submission = models.OneToOneField(HomeworkSubmission, on_delete=models.CASCADE, related_name='review')
    # Baho bergan o'qituvchi
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='reviews')
    # O'qituvchining izohi
    comment = models.TextField(null=True, blank=True)
    # Berilgan ball
    ball = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"Review for {self.submission.student.user.phone_number} - {self.submission.homework.title}"

    class Meta:
        verbose_name = 'Uy vazifasini baholash'
        verbose_name_plural = 'Uy vazifalarini baholashlar'