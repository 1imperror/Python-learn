from django.http import HttpResponse
from django.shortcuts import render
from .UserRegister import UserReg
from .models import Buyer, Game
from django.core.paginator import Paginator


# Create your views here.
def platform_page(request):
    return render(request, 'platform.html')


def games_page(request):
    games = Game.objects.all()
    context = {'games': games}
    return render(request, 'games.html', context)


def cart_page(request):
    return render(request, 'cart.html')


def sign_up_by_html(request):
    users = Buyer.objects.all()
    info = {}
    context = info
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        if password == repeat_password and int(age) >= 18 and username not in [user.name for user in users]:
            Buyer.objects.create(name=username, balance=0, age=age)
            return HttpResponse(f'Приветствуем, {username}!')
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif username in [user.name for user in users]:
            info['error'] = 'Пользователь уже существует'
    return render(request, 'registration_page.html', context)


def sign_up_by_django(request):
    users = Buyer.objects.all()
    info = {}
    if request.method == 'POST':
        form = UserReg(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if password == repeat_password and int(age) >= 18 and username not in [user.name for user in users]:
                Buyer.objects.create(name=username, balance=0, age=age)
                return HttpResponse(f'Приветствуем, {username}!')
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif username in [user.name for user in users]:
                info['error'] = 'Пользователь уже существует'
    else:
        form = UserReg()
    info['form'] = form
    return render(request, 'registration_page.html', context=info)


def game_list(request):
    options = [5, 10, 20, 50, 100]
    per_page = request.GET.get('per_page', 5)
    try:
        per_page = int(per_page)
        if per_page <= 0:
            per_page = 10
    except ValueError:
        per_page = 10

    articles = Game.objects.all()

    paginator = Paginator(articles, per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'per_page': per_page,
        'options': options,
    }
    return render(request, 'game_list.html', context)


