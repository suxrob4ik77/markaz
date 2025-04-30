from ..models import *
from django.db import models
from .student_model import *

# Oy modeli - to'lov oylari
class Month(BaseModel):
    # Oyning nomi
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Oy'
        verbose_name_plural = 'Oylar'


# To'lov turi modeli - to'lov turlari
class PaymentType(BaseModel):
    # To'lov turining nomi
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'To\'lov turi'
        verbose_name_plural = 'To\'lov turlari'


# To'lov modeli - talabalarning to'lovlari
class Payment(BaseModel):
    # To'lov qilgan talaba
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='payment')
    # To'lov qilingan guruh
    group = models.ForeignKey(GroupStudent, on_delete=models.SET_NULL, related_name='payment', null=True, blank=True)
    # To'lov qilingan oy
    month = models.ForeignKey(Month, on_delete=models.CASCADE, related_name='payment', null=True, blank=True)
    # To'lov turi
    payment_type = models.ForeignKey(PaymentType, on_delete=models.CASCADE, related_name='payment')
    # To'lov summasi
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.student.user.phone_number} - {self.price} UZS ({self.payment_type.title})"

    class Meta:
        verbose_name = 'To\'lov'
        verbose_name_plural = 'To\'lovlar'