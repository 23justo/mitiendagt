from django.urls import path

# View
from stores import views


urlpatterns = [

    # Management
    path(
        route='',
        view=views.StoreView.as_view(),
        name='home'
    ),

]
