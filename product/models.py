from django.contrib.auth import get_user_model
from django.db import models

from account.models import Doctor
from category.models import Category

User=get_user_model()

class Product(models.Model):
    STATUS_CHOICES=(('in_stock','в наличии'),
                    ('out_stock','Нет в наличии'))
    owner=models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    title=models.CharField(max_length=250)
    category=models.ForeignKey(Category,on_delete=models.CASCADE, related_name='products')
    description=models.TextField(blank=True, null=True)
    image=models.ImageField(upload_to='images')
    price=models.DecimalField(max_digits=9, decimal_places=2)
    stock=models.CharField(max_length=50, choices=STATUS_CHOICES)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name='Лекарственный препарат'
        verbose_name_plural='Лекарственные препараты'


# class Talon(models.Model):
#     # STATUS_CHOICES = (('have', 'есть '),
#     #                   ('not_have', 'Нету талон'))
#     # doctor=models.ForeignKey(Doctor, on_delete=models.CASCADE,)
#
#     patientName = models.CharField(max_length=40, null=True)
#     doctorName = models.CharField(max_length=40, null=True)
#     appointmentDate = models.DateField(auto_now=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     symptoms = models.CharField(max_length=40, null=True)
#     _id = models.CharField(max_length=40, null=True)
#     address = models.CharField(max_length=40)
#     mobile = models.CharField(max_length=20,null=True)
#     email = models.EmailField(unique=True)
#
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         verbose_name = 'Талон'
#         verbose_name_plural = 'Талон'
# class Appointment(models.Model):
#     STATUS_CHOICES=(('have','есть талон'),
#                     ('not_have','Нету талон'))
#     # doctor=models.ForeignKey(Doctor, on_delete=models.CASCADE,)
#     patientName=models.CharField(max_length=40,null=True)
#     doctorName=models.CharField(max_length=40,null=True)
#     appointmentDate=models.DateField(auto_now=True)
#     created_at=models.DateTimeField(auto_now_add=True)
#     # stock = models.CharField(max_length=50, choices=STATUS_CHOICES)
#     talon=models.ManyToManyField(Talon, )
#
#
#     def __str__(self):
#         return self.title
#     class Meta:
#         verbose_name='Встреча'
#         verbose_name_plural='Встреча'

class Talon(models.Model):
    _id = models.CharField(max_length=40, null=True)
    address = models.CharField(max_length=40)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self._id

    class Meta:
        verbose_name = 'Талон'
        verbose_name_plural = 'Талоны'


class Appointment(models.Model):
    appointmentDate = models.DateField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    talon = models.ManyToManyField(Talon)

    def __str__(self):
        return f'Appointment on {self.appointmentDate}'

    class Meta:
        verbose_name = 'Встреча'
        verbose_name_plural = 'Встречи'

# class Appointment(models.Model):
#     patientId=models.PositiveIntegerField(null=True)
#     doctorId=models.PositiveIntegerField(null=True)
#     patientName=models.CharField(max_length=40,null=True)
#     doctorName=models.CharField(max_length=40,null=True)
#     appointmentDate=models.DateField(auto_now=True)
#     description=models.TextField(max_length=500)
#     status=models.BooleanField(default=False)
#
#
#
# class PatientDischargeDetails(models.Model):
#     patientId=models.PositiveIntegerField(null=True)
#     patientName=models.CharField(max_length=40)
#     assignedDoctorName=models.CharField(max_length=40)
#     address = models.CharField(max_length=40)
#     mobile = models.CharField(max_length=20,null=True)
#     symptoms = models.CharField(max_length=100,null=True)
#
#     admitDate=models.DateField(null=False)
#     releaseDate=models.DateField(null=False)
#     daySpent=models.PositiveIntegerField(null=False)
#
#     roomCharge=models.PositiveIntegerField(null=False)
#     medicineCost=models.PositiveIntegerField(null=False)
#     doctorFee=models.PositiveIntegerField(null=False)
#     OtherCharge=models.PositiveIntegerField(null=False)
#     total=models.PositiveIntegerField(null=False)

# Create your models here.
