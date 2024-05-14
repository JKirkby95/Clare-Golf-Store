from django import forms
from .models import Appointment, Product, Fitter, Service
from products.models import Category
from datetime import datetime, time
from django.utils import timezone

class ClubFittingForm(forms.ModelForm):
    customer = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    appointment_time = forms.ChoiceField(
        choices=[], widget=forms.Select(attrs={"class": "form-control"})
    )
    club = forms.ModelChoiceField(
        queryset=Product.objects.none(),
        widget=forms.Select(attrs={"class": "form-control"}),
        empty_label="Select a Club"
    )
    fitter = forms.ModelChoiceField(
        queryset=Fitter.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        empty_label="Select a Fitter"
    )
    service = forms.ModelChoiceField(
        queryset=Service.objects.none(),  # Ensure the queryset is initialized as empty
        widget=forms.Select(attrs={"class": "form-control"}),
        empty_label="Select a Service"
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Filter products by specific categories
        category_names = ['Drivers', 'Woods', 'Irons', 'Wedges', 'Putters']
        categories = Category.objects.filter(name__in=category_names)
        self.fields['club'].queryset = Product.objects.filter(category__in=categories).distinct()

        time_slots = [("", "---------")]
        current_time = time(9, 0)
        while current_time <= time(17, 0):
            time_slots.append(
                (current_time.strftime("%H:%M"),
                 current_time.strftime("%I:%M %p"))
            )
            current_time = (
                current_time.replace(minute=current_time.minute + 30)
                if current_time.minute == 0
                else current_time.replace(hour=current_time.hour + 1, minute=0)
            )
        self.fields["appointment_time"].choices = time_slots

        # Populate the choices for the service field
        self.fields['service'].queryset = Service.objects.all()

    def clean_appointment_date(self):
        appointment_date = self.cleaned_data.get("appointment_date")
        if appointment_date is None:
            raise forms.ValidationError("Appointment date is required.")
        if appointment_date < timezone.now().date():
            raise forms.ValidationError("You can't select a date in the past.")
        return appointment_date

    def clean(self):
        cleaned_data = super().clean()
        appointment_time = cleaned_data.get("appointment_time")
        appointment_date = cleaned_data.get("appointment_date")

        if appointment_date and appointment_time:
            appointment_hour, appointment_minute = map(
                int, appointment_time.split(":")
            )
            appointment_time_obj = time(
                hour=appointment_hour, minute=appointment_minute
            )
            appointment_datetime = datetime.combine(
                appointment_date, appointment_time_obj
            )

            fitter = cleaned_data.get('fitter')
            if fitter and Appointment.objects.filter(
                fitter=fitter,
                appointment_date=appointment_date,
                appointment_time=appointment_time_obj,
            ).exists():
                raise forms.ValidationError(
                    f"{fitter.name} is booked at the selected time and date."
                )

        return cleaned_data

    class Meta:
        model = Appointment
        fields = [
            "appointment_date",
            "appointment_time",
            "customer",
            "club",
            "fitter",
            "service",  # Include the service field in the form
        ]
        widgets = {
            "appointment_date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "appointment_time": forms.TimeInput(attrs={"type": "time", "class": "form-control"}),
        }
