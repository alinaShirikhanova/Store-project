from django.shortcuts import render


def auth_user(request):
    return render(request, 'users/auth.html')

def register(request):
    return render(request, 'users/registration.html')
