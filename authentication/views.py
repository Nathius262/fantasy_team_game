from django.shortcuts import render, redirect


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    return render(request, "authentication/login.html")

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    return render(request, "authentication/signup.html")