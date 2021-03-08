from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView, TemplateView


from stores.models import Store
# Create your views here.

class StoreView(LoginRequiredMixin, TemplateView):
    """Return all published posts."""

    template_name = 'stores/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['store'] = Store.objects.get(pk = self.request.user.profile.store.pk)
        return context