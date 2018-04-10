from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy

from .models import Celebrity
from .forms import CelebrityForm


class CelebrityListView(ListView):
    template_name = 'celebrity/list.html'
    queryset = Celebrity.objects.all()


class CelebrityCreateView(CreateView):
    template_name = 'celebrity/create.html'
    queryset = Celebrity.objects.all()
    form_class = CelebrityForm
    success_url = reverse_lazy('celebrity:list')


class CelebrityUpdateView(UpdateView):
    template_name = 'celebrity/create.html'
    queryset = Celebrity.objects.all()
    form_class = CelebrityForm
    success_url = reverse_lazy('celebrity:list')
