from django.urls import path

from . import views

app_name = 'notification'
urlpatterns = [
    path('notification', views.NotificationAPIView.as_view(), name='notification'),
    path('celebrity/<str:celebrity_id>',
         views.NotificationCelebrityAPIView.as_view()),
]
