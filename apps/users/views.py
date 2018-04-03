from django.views.generic import ListView, CreateView, UpdateView, View
from django.urls import reverse_lazy
from rest_framework.generics import RetrieveUpdateAPIView, CreateAPIView

from .models import MyUser
from .forms import UserManagerForm, UserFanForm
from .serializers import MyUserFanSerializer, MyUserManagerSerializer


class UserFanListView(ListView):
    template_name = 'user/fan_list.html'
    queryset = MyUser.objects.user()


class UserFanUpdateView(UpdateView):
    template_name = 'user/fan_update.html'
    queryset = MyUser.objects.user()
    form_class = UserFanForm
    success_url = reverse_lazy('user:fan')


class UserFanAPIView(RetrieveUpdateAPIView):
    serializer_class = MyUserFanSerializer
    queryset = MyUser.objects.user()


class UserManagerListView(ListView):
    template_name = 'user/manager_list.html'
    queryset = MyUser.objects.manager()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = UserManagerForm()
        context.update({
            'form': form
        })
        return context


class UserManagerCreateAPIView(CreateAPIView):
    serializer_class = MyUserManagerSerializer
    queryset = MyUser.objects.manager()