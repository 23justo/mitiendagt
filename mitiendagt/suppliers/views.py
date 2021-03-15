from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import *
from django.urls import reverse_lazy

from suppliers import models, forms


class SupplierListView(LoginRequiredMixin, ListView):
    model = models.Supplier
    template_name = "suppliers/SupplierListView.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['suppliers'] = models.Supplier.objects.filter(store=self.request.user.profile.store)
        return context


class SupplierCreateView(CreateView):
    form_class = forms.SupplierForm
    template_name = "suppliers/SupplierCreateView.html"
    success_url = reverse_lazy('suppliers:SupplierListView')

    def form_valid(self, form):
        form.instance.store = self.request.user.profile.store
        form.save()
        return super().form_valid(form)


class SupplierUpdateView(LoginRequiredMixin, UpdateView):

    template_name = 'suppliers/SupplierUpdateView.html'
    model = models.Supplier
    fields = ['name', 'email', 'phone', 'address']
    success_url = reverse_lazy('suppliers:SupplierListView')


class SupplierDeleteView(LoginRequiredMixin, DeleteView):

    template_name = 'suppliers/SupplierDeleteView.html'
    context_object_name = 'supplier'
    model = models.Supplier
    fields = ['name', 'price', 'cost']
    success_url = reverse_lazy('suppliers:SupplierListView')