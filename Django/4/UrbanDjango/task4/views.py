from django.shortcuts import render


# Create your views here.
def platform_page(request):
    return render(request, 'platform.html')


def games_page(request):
    context = {'games': ["Atomic Heart", "Cyberpunk 2077", "PayDay 2"]}
    return render(request, 'games.html', context)


def cart_page(request):
    return render(request, 'cart.html')
