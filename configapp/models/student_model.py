from .group_model import *
from .teacher_model import *

# Talaba modeli - o'quv markazining talabalari
class Student(BaseModel):
    # Talabaning foydalanuvchi hisobi
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    # Talabaning guruhlari
    group = models.ManyToManyField(GroupStudent,related_name='get_student')
    # Talaba haqida qo'shimcha ma'lumot
    descreptions = models.CharField(max_length=200,blank=True,null=True)

    def __str__(self):
        return self.user.phone_number

    class Meta:
        verbose_name = 'Talaba'
        verbose_name_plural = 'Talabalar'

# Ota-ona modeli - talabalarning ota-onalari
class Parents(BaseModel):
    # Talaba
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    # Ota-onaning to'liq ismi
    full_name = models.CharField(max_length=50, null=True, blank=True)
    # Ota-onaning telefon raqami
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    # Ota-onaning manzili
    address = models.CharField(max_length=200, null=True, blank=True)
    # Ota-ona haqida qo'shimcha ma'lumot
    descriptions = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Ota-ona'
        verbose_name_plural = 'Ota-onalar'