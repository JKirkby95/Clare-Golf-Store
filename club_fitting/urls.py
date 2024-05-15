from django.urls import path
from . import views

urlpatterns = [
    path('appointments/', views.appointments_list, name='appointments'),
    path('book-appointment/', views.booking_view, name='book_appointment'),
    path('edit-appointment/<int:appointment_id>/', views.edit_appointment_view, name='edit_appointment'),
    path('delete-appointment/<int:appointment_id>/', views.delete_appointment_view, name='delete_appointment'),
]
 