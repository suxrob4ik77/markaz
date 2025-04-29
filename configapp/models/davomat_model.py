from django.db import models

from ..models import BaseModel
from ..models import Student
from ..models import GroupStudent


class Status(BaseModel):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'


class Davomat(BaseModel):
    group = models.ForeignKey(GroupStudent, on_delete=models.CASCADE, related_name='attendance')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendance')
    status = models.ForeignKey('Status', on_delete=models.CASCADE, related_name='attendance', null=True, blank=True)

    def __str__(self):
        return f"{self.student.user.phone_number} - {self.group.title}"

    class Meta:
        verbose_name = "Attendance"
        verbose_name_plural = "Attendances"

