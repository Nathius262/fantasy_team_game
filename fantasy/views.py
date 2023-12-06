from django.shortcuts import render

# Create your views here.

def index_view(request):
    if request.user.is_authenticated:
        return render(request, "fantasy/dashboard.html")
    else:
        return render(request, "fantasy/index.html")