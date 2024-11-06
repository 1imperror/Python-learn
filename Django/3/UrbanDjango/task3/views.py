from django.shortcuts import render


# Create your views here.
def platform_page(request):
    main_head = 'Главная страница'
    half_head = 'Главная'
    shop = 'Магазин'
    cart = 'Корзина'
    context = {
            'main': main_head,
            'half': half_head,
            'shop': shop,
            'cart': cart

    }
    return render(request, 'platform.html', context)


def games_page(request):
    main_head = 'Игры'
    atom = 'Atomic Heart'
    cyber = 'Cyberpunk 2077'
    pay = 'PayDay 2'
    back = 'Вернуться обратно'
    bye = 'Купить'
    context = {
            'main': main_head,
            'atom': atom,
            'cyber': cyber,
            'pay': pay,
            'back': back,
            'bye': bye

    }
    return render(request, 'games.html', context)


def cart_page(request):
    main_head = 'Извините, ваша корзина пуста'
    back = 'Вернуться обратно'
    context = {
        'main': main_head,
        'back': back

    }
    return render(request, 'cart.html', context)
