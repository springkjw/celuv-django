from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from .models import Celebrity


class CelebrityListView(ListView):
    template_name = 'celebrity/list.html'
    queryset = Celebrity.objects.all()


class CelebrityCreateView(CreateView):
    template_name = 'celebrity/create.html'
    queryset = Celebrity.objects.all()
    success_url = reverse_lazy('celebrity:list')
    fields = (
        'name',
        'celeb_type',
        'real_name',
        'debut',
        'birth',
        'sex',
    )
