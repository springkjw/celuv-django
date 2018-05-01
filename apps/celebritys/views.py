from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy

from .models import Celebrity
from .forms import CelebrityForm


class CelebrityListView(ListView):
    template_name = 'celebrity/list.html'
    queryset = Celebrity.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        entertainment = self.request.GET.get('entertainment')
        if entertainment:
            queryset = queryset.filter(entertainment__name__icontains=entertainment)
        if self.request.GET.get('name'):
            queryset = queryset.filter(name__icontains=self.request.GET.get('name'))
        if self.request.GET.get('celeb_type'):
            queryset = queryset.filter(celeb_type=self.request.GET.get('celeb_type'))
        return queryset


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
