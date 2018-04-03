from django.views.generic import RedirectView
from django.urls import reverse_lazy


class HomeView(RedirectView):
    url = reverse_lazy('celebrity:list')