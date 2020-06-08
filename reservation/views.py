from django.shortcuts import render
from .models import Reservation
from .forms import ReserveForm

# Create your views here.

def reserve(request):
    reserve_form = ReserveForm()

    if request.method == 'POST':
        reserve_form = ReserveForm(request.POST)
        if reserve_form.is_valid():
            reserve_form.save()

    context = {'form': reserve_form }
    return render(request, 'Reservation/reservation.html', context)