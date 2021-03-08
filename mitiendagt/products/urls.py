from django.urls import path

# View
from products import views


urlpatterns = [

    path(route='', view=views.ProductListView.as_view(), name='ProductListView'),
    path(route='create', view=views.ProductCreateView.as_view(), name='ProductCreateView'),
    path(route='update/<int:pk>', view=views.ProductUpdateView.as_view(), name='ProductUpdateView'),
    path(route='delete/<int:pk>', view=views.ProductDeleteView.as_view(), name='ProductDeleteView'),
]
