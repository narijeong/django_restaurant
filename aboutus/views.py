from django.shortcuts import render
from .models import AboutUs, Why_Choose_Us, Chef

# Create your views here.

def aboutus(request):
    aboutus = AboutUs.objects.last()
    why_choose_us = Why_Choose_Us.objects.all()
    chefs = Chef.objects.all()

    context = {
        'aboutus': aboutus,
        'why_choose_us': why_choose_us,
        'chefs': chefs,
    }

    return render(request, "aboutus/about.html", context)