from django.urls import path
from .views import login_view, signup_view
import allauth.account.views

app_name= "authenticate"

urlpatterns = [
    path('login/', login_view, name="login"),
    path('signup/', signup_view, name="signup"),
    path("logout/", allauth.account.views.logout, name="logout"),
]
