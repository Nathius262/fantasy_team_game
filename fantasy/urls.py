from django.urls import path
from .views import index_view, leadersboard_view, player_list_view, club_list_view

urlpatterns = [
    path("", index_view, name="index"),
    path("leadersboard", leadersboard_view, name="leadersboard"),
    path("players", player_list_view, name="player_list"),
    path("clubs", club_list_view, name="club_list"),
]