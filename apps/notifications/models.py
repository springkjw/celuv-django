from django.conf import settings
from django.db import models
from django.contrib.postgres.fields import ArrayField


class Notification(models.Model):
    NOTIFICATION_CELEBRITY = 'c'
    NOTIFICATION_SCHEDULE = 's'
    NOTIFICATION_TYPE = (
        (NOTIFICATION_CELEBRITY, '연예인'),
        (NOTIFICATION_SCHEDULE, '스케줄'),
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='유저'
    )
    notification_type = models.CharField(
        max_length=1,
        default=NOTIFICATION_CELEBRITY,
        choices=NOTIFICATION_TYPE,
        verbose_name='알림 유형'
    )
    target = ArrayField(
        models.CharField(
            max_length=255,
        ),
        default=[]
    )

    class Meta:
        db_table = 'notification'
        verbose_name = '알림'
        verbose_name_plural = '알림들'
