from django.shortcuts import render
from .models import Pasien

# Create your views here.
def home(request):
    pasiens = Pasien.objects.all()
    return render(request, 'home.html', {'pasiens':pasiens})
