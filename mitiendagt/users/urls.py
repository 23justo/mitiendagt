"""Users URLs."""

# Django
from django.urls import path

# View
from users import views


urlpatterns = [

    # Management
    path(
        route='login/',
        view=views.LoginView.as_view(),
        name='login'
    ),

]
