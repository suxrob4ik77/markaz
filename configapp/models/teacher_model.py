from django.db import models

from rest_framework import filters

from .auth_users import *


# Kurs modeli - o'quv markazida o'qitiladigan fanlar
class Course(BaseModel):
    # Kursning nomi
    title = models.CharField(max_length=50)
    # Kurs haqida qo'shimcha ma'lumot
    descriptions = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Kurs'
        verbose_name_plural = 'Kurslar'


# Bo'lim modeli - xodimlarning darajasini belgilash uchun
class Departments(BaseModel):
    # Bo'limning nomi
    title = models.CharField(max_length=50)
    # Bo'limning faol yoki faol emasligi
    is_active = models.BooleanField(default=True)
    # Bo'lim haqida qo'shimcha ma'lumot
    descriptions = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Bo\'lim'
        verbose_name_plural = 'Bo\'limlar'


# O'qituvchi modeli - o'qituvchilar ma'lumotlarini saqlash uchun
class Teacher(BaseModel):
    # O'qituvchining foydalanuvchi hisobi
    user = models.OneToOneField(User, on_delete=models.RESTRICT,related_name="teacher")
    # O'qituvchining bo'limlari
    departments = models.ManyToManyField(Departments, related_name='get_department')
    # O'qituvchining o'qitadigan kurslari
    course = models.ManyToManyField(Course, related_name='get_course')
    # O'qituvchi haqida qo'shimcha ma'lumot
    descriptions = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.user.phone_number

    class Meta:
        verbose_name = 'O\'qituvchi'
        verbose_name_plural = 'O\'qituvchilar'