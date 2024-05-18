from django.urls import path
from . import views
from .views import contact_view, shipping_view, payment_view, privacy_view, about_view

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', contact_view, name='contact'),
    path('shipping/', shipping_view, name='shipping'),
    path('payment/', payment_view, name='payment'),
    path('privacy/', privacy_view, name='privacy'),
    path('about/', about_view, name='about'),
]