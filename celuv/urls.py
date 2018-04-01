from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from .views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('celebrity/', include('apps.celebritys.urls', namespace='celebrity')),
    path('entertainment/', include('apps.entertainments.urls',
                                   namespace='entertainment')),
    path('schedule/', include('apps.schedules.urls', namespace='schedule')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
