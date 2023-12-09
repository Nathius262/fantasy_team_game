from django.urls import path
from .views import squad_view, UserTeamListViewSet, CreateUserTeamViewSet

app_name = "user"

urlpatterns = [
    path("squad/", squad_view, name="squad"), 
    path("api/squad/add/", UserTeamListViewSet.as_view(), name="add_squad"),
    path("api/squad/create-user-team/", CreateUserTeamViewSet.as_view(), name="create_squad"),
]
