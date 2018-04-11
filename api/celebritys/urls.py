from django.urls import path

from .views import CelebrityLikeListAPIView

app_name = 'celebrity'
urlpatterns = [
    path('like/', CelebrityLikeListAPIView.as_view(), name='like_list'),
]