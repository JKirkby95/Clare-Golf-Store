from django.db import models
from products.models import Product
from profiles.models import UserProfile


class Fitter(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    customer = models.CharField(max_length=100)
    fitter = models.ForeignKey(Fitter, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    club = models.ForeignKey(Product, on_delete=models.CASCADE)
    notes = models.TextField(blank=True, null=True)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.customer} - {self.appointment_date} at {self.appointment_time}"
