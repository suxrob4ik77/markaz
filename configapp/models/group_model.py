# from pickletools import string4
# from tkinter.constants import CASCADE
#
# from django.template.defaultfilters import time
#
# from .auth_users import *
# from .model_teacher import *
#
#
# class Rooms(BaseModel):
#     title = models.CharField(max_length=50)
#     descriptions = models.CharField(max_length=500,blank=True,null=True)
#
#     def __str__(self):
#         return self.title
#
#
# class TableType(BaseModel):
#     title = models.CharField(max_length=50)
#     descriptions = models.CharField(max_length=500,blank=True,null=True)
#
#     def __str__(self):
#         return self.title
#
#
# class Table(BaseModel):
#     start_time = models.TimeField()
#     end_time = models.TimeField()
#     room = models.ForeignKey(Rooms, on_delete=models.RESTRICT)
#     type = models.ForeignKey(TableType, on_delete=models.RESTRICT)
#     descriptions = models.CharField(max_length=500, blank=True, null=True)
#
#     def __str__(self):
#         return f"{self.start_time} - {self.end_time}"
#
#
#
#
# class GroupStudent(BaseModel):
#     title = models.CharField(max_length=40, unique=True)
#     course = models.ForeignKey(Course, on_delete=models.RESTRICT,related_name='course')
#     teacher = models.ManyToManyField(Teacher, related_name='teacher_get')
#     table = models.ForeignKey(Table,on_delete=models.CASCADE)
#     start_time = models.DateField()
#     end_time = models.DateField()
#     descriptions = models.CharField(max_length=500,blank=True,null=True)
#
#     def __str__(self):
#         return self.title
#

from django.db import models
from .auth_users import *
from .teacher_model import *
from .student_model import *

# Xona modeli - dars o'tiladigan xonalar
class Rooms(models.Model):
    # Xonaning nomi
    title = models.CharField(max_length=50)
    # Xona haqida qo'shimcha ma'lumot
    descriptions = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Xona'
        verbose_name_plural = 'Xonalar'

# Jadval turi modeli - dars jadvalining turlari
class TableType(BaseModel):
    # Jadval turining nomi
    title = models.CharField(max_length=50)
    # Jadval turi haqida qo'shimcha ma'lumot
    descriptions = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Jadval turi'
        verbose_name_plural = 'Jadval turlari'

# Jadval modeli - dars jadvali
class Table(BaseModel):
    # Darsning boshlanish vaqti
    start_time = models.TimeField()
    # Darsning tugash vaqti
    end_time = models.TimeField()
    # Dars o'tiladigan xona
    room = models.ForeignKey(Rooms, on_delete=models.RESTRICT)
    # Jadval turi
    type = models.ForeignKey(TableType, on_delete=models.RESTRICT)
    # Jadval haqida qo'shimcha ma'lumot
    descriptions = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.start_time.__str__()+" "+self.end_time.__str__()

    class Meta:
        verbose_name = 'Jadval'
        verbose_name_plural = 'Jadvallar'

# Guruh modeli - talabalar guruhi
class GroupStudent(BaseModel):
    # Guruhning nomi
    title = models.CharField(max_length=50, unique=True)
    # Guruhning kursi
    course = models.ForeignKey(Course, on_delete=models.RESTRICT)
    # Guruhning o'qituvchilari
    teacher = models.ManyToManyField(Teacher, related_name='get_teacher')
    # Guruhning dars jadvali
    table = models.ForeignKey(Table, on_delete=models.RESTRICT)
    # Guruhning boshlanish sanasi
    start_date = models.DateField()
    # Guruhning tugash sanasi
    end_date = models.DateField(null=True, blank=True)
    # Guruh haqida qo'shimcha ma'lumot
    descriptions = models.CharField(max_length=500, blank=True, null=True)
    # Guruhning faol yoki faol emasligi
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Guruh'
        verbose_name_plural = 'Guruhlar'

# Fan modeli - o'qitiladigan fanlar
class Subject(BaseModel):
    # Fanning nomi
    title = models.CharField(max_length=50)
    # Fan haqida qo'shimcha ma'lumot
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Fan'
        verbose_name_plural = 'Fanlar'
