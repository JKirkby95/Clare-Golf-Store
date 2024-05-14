from django.contrib import admin
from .models import Fitter, Appointment, Service

class FitterAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'phone',
    )


class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'price',
    )


class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        'customer',
        'appointment_date',
        'appointment_time',
        'fitter',
        'club',
        'service',
        'user_profile',
        'notes',
    )

# Register the models with their respective admin classes
admin.site.register(Fitter, FitterAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Appointment, AppointmentAdmin)
