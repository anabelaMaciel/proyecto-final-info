from django.urls import path
from .views import SignUpView, LoginView
from django.contrib.auth.views import LogoutView

app_name = "apps.blog_auth"

urlpatterns = [
    path("register/", SignUpView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="/auth/login/"), name="logout"),

]
