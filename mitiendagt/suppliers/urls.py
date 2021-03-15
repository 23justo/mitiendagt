from django.urls import path

# View
from suppliers import views


urlpatterns = [

    path(route='', view=views.SupplierListView.as_view(), name='SupplierListView'),
    path(route='create', view=views.SupplierCreateView.as_view(), name='SupplierCreateView'),
    path(route='update/<int:pk>', view=views.SupplierUpdateView.as_view(), name='SupplierUpdateView'),
    path(route='delete/<int:pk>', view=views.SupplierDeleteView.as_view(), name='SupplierDeleteView'),
]
