from django.urls import path

from .views import CelebrityListView, CelebrityCreateView, CelebrityUpdateView

app_name = 'celebrity'
urlpatterns = [
    path('list', CelebrityListView.as_view(), name='list'),
    path('create', CelebrityCreateView.as_view(), name='create'),
    path('<int:pk>/update', CelebrityUpdateView.as_view(), name='update'),
]
