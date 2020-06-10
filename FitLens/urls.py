from django.urls import path
from .views import lens, contactus

urlpatterns = [
    path('', lens, name='FitLens'),
    path('contactus/', contactus, name="Contact us"),
]