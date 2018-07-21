from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('', include('apps.bases.urls', namespace='base')),
    path('user/', include('apps.users.urls', namespace='user')),
    path('celebrity/', include('apps.celebritys.urls', namespace='celebrity')),
    path('entertainment/', include('apps.entertainments.urls',
                                   namespace='entertainment')),
    path('schedule/', include('apps.schedules.urls', namespace='schedule')),
    path('feedback/', include('apps.feedbacks.urls', namespace='feedback')),
    path('api/v1/', include('api.urls', namespace='api')),
    path('select2/', include('django_select2.urls')),
    path('admin/', admin.site.urls),
    path('docs/', schema_view),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
