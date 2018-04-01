from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from .models import Entertainment
from .forms import EntertainmentForm


class EntertainmentListView(ListView):
    template_name = 'entertainment/list.html'
    queryset = Entertainment.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')
        if search is not None:
            queryset = queryset.filter(name__icontains=search)
        return queryset


class EntertainmentCreateView(CreateView):
    models = Entertainment
    form_class = Entertainment
    success_url = reverse_lazy('entertainment:list')
