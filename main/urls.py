
from django.urls import path
from .views import (
    HomeView,
    SearchView,
    user_login_view,
    user_logout_view,
    normal_user_registration_view,
    choose_account_type_view 
    )

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("search/", SearchView, name="searching"),
    path("login/",  user_login_view, name="login"),
    path("logout/", user_logout_view, name="logout"),
    path("signup/", choose_account_type_view, name="choose"),
    path('register/',  normal_user_registration_view, name="register"),
]