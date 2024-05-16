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
            # Process the data in form.cleaned_data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Send an email (for example)
            send_mail(
                f'Message from {name}',
                message,
                email,
                ['jkirkby95@gmail.com'],
            )
            return render(request, 'contact/success.html')
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})
