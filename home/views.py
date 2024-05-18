from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save()
            # Optionally send an email
            send_mail(
                f'Message from {contact_message.name}',
                contact_message.message,
                contact_message.email,
                ['your_email@example.com'],  # Replace with your email address
            )
            return render(request, 'home/contact_success.html')
    else:
        form = ContactForm()
    return render(request, 'home/contact.html', {'form': form})


def shipping_view(request):
    """ A view to return the shipping page """

    return render(request, 'home/shipping.html')


def payment_view(request):
    """ A view to return the payment options page """

    return render(request, 'home/payment.html')


def privacy_view(request):
    """ A view to return the privacy policies page """

    return render(request, 'home/privacy_policy.html')


def about_view(request):
    """ A view to return the about us page """

    return render(request, 'home/about.html')