from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .models import UserProfile, Wishlist
from .forms import UserProfileForm
from products.models import Product

from checkout.models import Order


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)
    wishlist = get_object_or_404(Wishlist, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(
                request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True,
        "wishlist": wishlist,
    }

    return render(request, template, context)


@login_required
def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


@login_required
def wishlist_view(request):
    """ Display user's wishlist. """
    wishlist = get_object_or_404(Wishlist, user=request.user)
    template = 'profiles/profile.html'  
    context = {
        'wishlist': wishlist,
        'from_profile': True,  
    }
    return render(request, template, context)


@login_required
def add_to_wishlist(request, item_id):
    """ Add a product to the user's wishlist """

    product = get_object_or_404(Product, pk=item_id)
    redirect_url = request.POST.get('redirect_url')
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)

    if product in wishlist.products.all():
        messages.info(request, f"{product.name} is already on your Wishlist!")
    else:
        wishlist.products.add(product)
        messages.success(request, f"{product.name} has been added to your Wishlist!")

    return redirect('profile')


@login_required
def remove_from_wishlist(request, item_id):
    """ Removing a product from the user's wishlist """

    try:
        product = get_object_or_404(Product, pk=item_id)
        wishlist = get_object_or_404(Wishlist, user=request.user)

        if product in wishlist.products.all():
            wishlist.products.remove(product)
            messages.success(request, f"{product.name} has been removed from your Wishlist!")
            return HttpResponse(status=200)
        else:
            messages.info(request, f"{product.name} is not in your Wishlist.")
            return HttpResponse(status=404)

    except Exception as e:
        messages.error(request, f'Error removing item from wishlist: {e}')
        return HttpResponse(status=500)

