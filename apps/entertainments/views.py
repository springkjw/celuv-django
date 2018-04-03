from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Entertainment
from .forms import EntertainmentForm
from .serializers import EntertainmentSerializer


class EntertainmentListView(ListView):
    template_name = 'entertainment/list.html'
    queryset = Entertainment.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')
        if search is not None:
            queryset = queryset.filter(name__icontains=search)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = EntertainmentForm()
        context.update({
            'form': form,
        })
        return context


class EntertainmentCreateAPIView(CreateAPIView):
    serializer_class = EntertainmentSerializer
    queryset = Entertainment.objects.all()


class EntertainmentAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = EntertainmentSerializer
    queryset = Entertainment.objects.all()

    def post(self, request, *args, **kwargs):
        return self.patch(request, *args, **kwargs)