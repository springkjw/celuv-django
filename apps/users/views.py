from django.views.generic import (
    ListView, CreateView, UpdateView,
    View
)
from django.urls import reverse_lazy
from django.db import transaction
from django.contrib.auth.views import LoginView, LogoutView
from rest_framework.generics import RetrieveUpdateAPIView, CreateAPIView

from .models import MyUser
from .forms import UserManagerForm, UserFanForm, ManagerFormSet
from .serializers import MyUserFanSerializer, MyUserManagerSerializer


class UserLoginView(LoginView):
    template_name = 'user/login.html'
    success_url = reverse_lazy('base:home')


class UserLogoutView(LogoutView):
    pass


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


class UserManagerCreateView(CreateView):
    # 소속사 매니저 생성 페이지
    template_name = 'user/manager_create.html'
    model = MyUser
    form_class = UserManagerForm
    success_url = reverse_lazy('user:manager')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            formset = ManagerFormSet(self.request.POST)
        else:
            formset = ManagerFormSet()
        context.update({
            'formset': formset
        })
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        manager = context['formset']
        with transaction.atomic():
            self.object = form.save()
            if manager.is_valid():
                manager.instance = self.object
                manager.save()
        return super().form_valid(form)