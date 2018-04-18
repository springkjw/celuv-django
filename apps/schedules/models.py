from django.db import models
from django.urls import reverse_lazy
from apps.celebritys.models import Celebrity


class Schedule(models.Model):
    title = models.CharField(
        max_length=150,
        verbose_name='스케줄명'
    )
    schedule = models.DateTimeField(
        verbose_name='일정'
    )
    celebrity = models.ManyToManyField(
        Celebrity,
        verbose_name='출연 셀럽'
    )

    class Meta:
        db_table = 'schedule'
        verbose_name = '스케줄'
        verbose_name_plural = '스케줄들'

    def __str__(self):
        return self.title

    def get_celebrity(self):
        return [celebrity.name for celebrity in self.celebrity.all()]

    @property
    def get_absolute_url(self):
        return reverse_lazy('schedule:detail', kwargs={'pk': self.pk})

    @property
    def get_delete_url(self):
        return reverse_lazy('schedule:delete', kwargs={'pk': self.pk})


class ScheduleCategory(models.Model):
    SCHEDULE_RADIO = 'r'
    SCHEDULE_TV = 't'
    SCHEDULE_CONSERT = 'c'
    SCHEDULE_ALBUM = 'a'
    SCHEDULE_PHOTO = 'p'
    SCHEDULE_FAN = 'f'
    SCHEDULE_ETC = 'e'
    SCHEDULE_TYPE = (
        (SCHEDULE_RADIO, '라디오 스케줄'),
        (SCHEDULE_TV, '티비 스케줄'),
        (SCHEDULE_CONSERT, '공연행사'),
        (SCHEDULE_ALBUM, '앨범발매'),
        (SCHEDULE_PHOTO, '촬영'),
        (SCHEDULE_FAN, '팬미팅'),
        (SCHEDULE_ETC, '기타'),
    )

    schedule = models.ForeignKey(
        Schedule,
        on_delete=models.CASCADE,
        verbose_name='스케줄'
    )
    first_category = models.CharField(
        max_length=5,
        choices=SCHEDULE_TYPE,
        default=SCHEDULE_TV,
        verbose_name='상위 카테고리'
    )
    second_category = models.CharField(
        max_length=5,
        null=True,
        blank=True,
        verbose_name='하위 카테고리'
    )
    content = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='부가정보'
    )

    class Meta:
        db_table = 'schedule_category'
        verbose_name = '스케줄 카테고리'
        verbose_name_plural = '스케줄 카테고리들'

    def __str__(self):
        return self.first_category