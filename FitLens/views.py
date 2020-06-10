from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

def lens(request):
    return HttpResponse("<h1>What's new in your tribe? </h1>")


def contactus(request):
    return HttpResponse("<h1>Contact us at radojkovic.n@gmail.com</h1>")