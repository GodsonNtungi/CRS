from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {})


def bylocation(request):
<<<<<<< HEAD
    return render(request, 'bylocation.html', {})


def bysoil(request):
    return render(request, 'bysoil.html', {})


def bycrop(request):
    return render(request, 'bycrop.html', {})


def services(request):
    return render(request, 'services.html')


=======
    return render(request, 'bylocation.html')


def bysoil(request):
    return render(request, 'bysoil.html')


def bycrop(request):
    return render(request, 'bycrop.html')
>>>>>>> fc9c4496a838b5269544c36c35ffa0f954630b8d
