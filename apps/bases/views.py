from django.views.generic import RedirectView, TemplateView
from django.urls import reverse_lazy


class HomeView(RedirectView):
    url = reverse_lazy('celebrity:list')


class PrivateView(TemplateView):
    template_name = 'private.html'
