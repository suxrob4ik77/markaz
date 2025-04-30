from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# Asosiy model - barcha modellar uchun umumiy maydonlar
class BaseModel(models.Model):
    # Yaratilgan sana
    created_at = models.DateField(auto_now_add=True)
    # Yangilangan sana
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True

# Foydalanuvchi menejeri - foydalanuvchilarni boshqarish uchun
class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, email=None, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('Phone_number maydoni bo`lishi kerak emas!')
        # phone_number = self.normalize_phone_number(phone_number)
        user = self.model(phone_number=phone_number, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password, email=None, **extra_fields):
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_admin') is not True:
            raise ValueError('Superuser is_admin=True bo`lishi kerak!')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser is_staff=True bo`lishi kerak!')

        return self.create_user(phone_number, email, password, **extra_fields)

# Foydalanuvchi modeli - tizim foydalanuvchilari
class User(AbstractBaseUser, PermissionsMixin):
    # Telefon raqam validatori
    phone_regex = RegexValidator(
        regex=r'^\+998\d{9}$',
        message="Telefon raqam '+998XXXXXXXXX' formatida bo'lishi kerak!"
    )
    # Foydalanuvchi elektron pochtasi
    email = models.EmailField(unique=True, null=True, blank=True)
    # Foydalanuvchi telefon raqami
    phone_number = models.CharField(validators=[phone_regex], max_length=13, unique=True)
    # Foydalanuvchi admin yoki yo'qligi
    is_admin = models.BooleanField(default=False)
    # Foydalanuvchi xodim yoki yo'qligi
    is_staff = models.BooleanField(default=False)
    # Foydalanuvchi faol yoki yo'qligi
    is_active = models.BooleanField(default=True)
    # Foydalanuvchi talaba yoki yo'qligi
    is_student = models.BooleanField(default=False)
    # Foydalanuvchi o'qituvchi yoki yo'qligi
    is_teacher = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.phone_number

    @property
    def is_superuser(self):
        return self.is_admin

    class Meta:
        verbose_name = 'Foydalanuvchi'
        verbose_name_plural = 'Foydalanuvchilar'



