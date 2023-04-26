from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {})


def bylocation(request):
    return render(request, 'bylocation.html')


def bysoil(request):
    return render(request, 'bysoil.html')


def bycrop(request):
    return render(request, 'bycrop.html')