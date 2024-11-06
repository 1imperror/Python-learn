from django.shortcuts import render


# Create your views here.
def platform_page(request):
    return render(request, 'platform.html')


def games_page(request):
    return render(request, 'games.html')


def cart_page(request):
    return render(request, 'cart.html')
