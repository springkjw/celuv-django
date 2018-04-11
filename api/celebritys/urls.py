from django.urls import path

from .views import CelebrityLikeListAPIView, CelebrityListAPIView

app_name = 'celebrity'
urlpatterns = [
    path('', CelebrityListAPIView.as_view(), name='list'),
    path('like/', CelebrityLikeListAPIView.as_view(), name='like_list'),
]