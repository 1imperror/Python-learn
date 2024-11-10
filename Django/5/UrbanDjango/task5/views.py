from django.http import HttpResponse
from django.shortcuts import render
from .UserRegister import UserReg


# Create your views here.
def sign_up_by_html(request):
    users = ['Naowh', 'JdotB', 'DrJay', 'Meeres', 'Dorki']
    info = {}
    context = info
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        if password == repeat_password and int(age) >= 18 and username not in users:
            return HttpResponse(f'Приветствуем, {username}!')
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif username in users:
            info['error'] = 'Пользователь уже существует'
    return render(request, 'registration_page.html', context)


def sign_up_by_django(request):
    users = ['Naowh', 'JdotB', 'DrJay', 'Meeres', 'Dorki']
    info = {}
    if request.method == 'POST':
        form = UserReg(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if password == repeat_password and int(age) >= 18 and username not in users:
                return HttpResponse(f'Приветствуем, {username}!')
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif username in users:
                info['error'] = 'Пользователь уже существует'
    else:
        form = UserReg()
    info['form'] = form
    return render(request, 'registration_page.html', context=info)
