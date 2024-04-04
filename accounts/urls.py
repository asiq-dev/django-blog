from django.urls import path
from . import views


urlpatterns = [
    path("signup/", views.SingUpView.as_view(), name="signup"),
    # path("logout/", views.custom_logout, name="logout"),
]
