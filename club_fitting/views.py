from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ClubFittingForm
from .models import Appointment
from profiles.models import UserProfile

@login_required
def appointments_list(request):
    """
    Function-based view for displaying a list of appointments
    """
    user_profile = get_object_or_404(UserProfile, user=request.user)
    user_appointments = Appointment.objects.filter(user_profile=user_profile)
    return render(request, "club_fitting/appointments_list.html", {"appointments": user_appointments})

@login_required
def booking_view(request):
    """
    Function-based view for club fitting appointment booking page
    """
    template_name = "club_fitting/booking.html"
    if request.method == 'POST':
        form = ClubFittingForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            user_profile = UserProfile.objects.get(user=request.user)
            appointment.user_profile = user_profile
            appointment.save()
            messages.success(request, "Booking confirmed. Appointment details below.")
            return redirect("appointments")
    else:
        form = ClubFittingForm()
    return render(request, template_name, {"form": form})


@login_required
def edit_appointment_view(request, appointment_id):
    """
    Function-based view for editing club fitting appointments
    """
    template_name = "club_fitting/edit_appointment.html"
    appointment = get_object_or_404(Appointment, id=appointment_id)
    if appointment.user_profile.user != request.user:
        return redirect("userauth")
    if request.method == 'POST':
        form = ClubFittingForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            messages.success(request, "Appointment updated successfully.")
            return redirect("appointments")
    else:
        form = ClubFittingForm(instance=appointment)
    return render(request, template_name, {"form": form, "appointment_id": appointment_id})

@login_required
def delete_appointment_view(request, appointment_id):
    """
    Function-based view for deleting club fitting appointments
    """
    appointment = get_object_or_404(Appointment, id=appointment_id)
    if appointment.user_profile.user == request.user:
        appointment.delete()
        messages.success(request, "Appointment deleted successfully.")
    return redirect("appointments")
