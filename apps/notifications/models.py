from django.conf import settings
from django.db import models


class Notification(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='유저'
    )
    # is_active = models.C

    class Meta:
        db_table = 'notification'
        verbose_name = '알림'
        verbose_name_plural = '알림들'
