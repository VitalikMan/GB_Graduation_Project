from django.shortcuts import render


def login(request):
    context = {
        'title': 'Home - Авторизация',
    }
    return render(request, 'users/login.html', context)


def registration(request):
    context = {
        'title': 'Home - Регистрация',
    }
    return render(request,'users/registration.html', context)


def profile(request):
    context = {
        'title': 'Home - Профиль',
    }
    return render(request, 'users/profile.html', context)


def logout(request):
    context = {
        'title': 'Home - Выход',
    }
    return render(request, 'users/logout.html', context)
