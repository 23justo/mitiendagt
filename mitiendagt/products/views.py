from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import *
from django.urls import reverse_lazy

from products.models import Product

from products.forms import ProductForm

class ProductListView(LoginRequiredMixin, ListView):

    template_name = 'products/ProductListView.html'
    model = Product
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(store=self.request.user.profile.store)
        return context

class ProductCreateView(LoginRequiredMixin, CreateView):

    template_name = 'products/ProductCreateView.html'
    form_class = ProductForm
    success_url = reverse_lazy('products:ProductListView')

    def form_valid(self, form):
        form.instance.store = self.request.user.profile.store
        form.save()
        return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin, UpdateView):

    template_name = 'products/ProductUpdateView.html'
    model = Product
    fields = ['name', 'price', 'cost']
    success_url = reverse_lazy('products:ProductListView')

class ProductDeleteView(LoginRequiredMixin, DeleteView):

    template_name = 'products/ProductDeleteView.html'
    context_object_name = 'product'
    model = Product
    fields = ['name', 'price', 'cost']
    success_url = reverse_lazy('products:ProductListView')




