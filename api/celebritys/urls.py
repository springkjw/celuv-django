from django.urls import path

from .views import (
    CelebrityLikeListAPIView, CelebrityListAPIView,
    CelebrityLikeAPIView,
)

app_name = 'celebrity'
urlpatterns = [
    path('celebrity', CelebrityListAPIView.as_view(), name='list'),
    path('celebrity/<int:pk>/like', CelebrityLikeAPIView.as_view(), name='like'),
    path('like/', CelebrityLikeListAPIView.as_view(), name='like_list'),
]
