from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('apps.bases.urls', namespace='base')),
    path('user/', include('apps.users.urls', namespace='user')),
    path('celebrity/', include('apps.celebritys.urls', namespace='celebrity')),
    path('entertainment/', include('apps.entertainments.urls',
                                   namespace='entertainment')),
    path('schedule/', include('apps.schedules.urls', namespace='schedule')),
    path('select2/', include('django_select2.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
