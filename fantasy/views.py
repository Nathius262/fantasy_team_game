from django.shortcuts import render, redirect
from .models import PlayerTeam, Team
import random
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from operator import attrgetter

# Create your views here.
POSTS_PER_PAGE = 50

def index_view(request):
    if request.user.is_authenticated:
        return render(request, "fantasy/dashboard.html")
    else:
        return render(request, "fantasy/index.html")
    
def leadersboard_view(request):
    if request.user.is_authenticated:
        random_objects = sorted(PlayerTeam.objects.all(), key=lambda x: x.player_id.point, reverse=True)[:80]
        # Pagination
        page = request.GET.get('page', 1)
        POSTS_PER_PAGE = 20
        paginator = Paginator(random_objects, POSTS_PER_PAGE)

        try:
            random_objects = paginator.page(page)
        except PageNotAnInteger:
            random_objects = paginator.page(POSTS_PER_PAGE)
        except EmptyPage:
            random_objects = paginator.page(paginator.num_pages)
        context = {
            "objects":random_objects
        }
        
        return render(request, "fantasy/leadersboard.html", context)
    
    else:
        return redirect('index')
    
def player_list_view(request):
    random_objects = sorted(PlayerTeam.objects.all(), key=lambda x: random.random())
    # Pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(random_objects, POSTS_PER_PAGE)

    try:
        random_objects = paginator.page(page)
    except PageNotAnInteger:
        random_objects = paginator.page(POSTS_PER_PAGE)
    except EmptyPage:
        random_objects = paginator.page(paginator.num_pages)
    context = {
        "objects":random_objects
    }
    return render(request, "fantasy/player_list.html", context)

def club_list_view(request):
    random_objects = sorted(Team.objects.all(), key=lambda x: x.cid)
    #random_objects = Team.objects.all()
    # Pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(random_objects, POSTS_PER_PAGE)

    try:
        random_objects = paginator.page(page)
    except PageNotAnInteger:
        random_objects = paginator.page(POSTS_PER_PAGE)
    except EmptyPage:
        random_objects = paginator.page(paginator.num_pages)
    context = {
        "objects":random_objects
    }
    return render(request, "fantasy/club_list.html", context)