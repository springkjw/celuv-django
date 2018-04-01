from django.db import models
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


class ScheduleCategory(models.Model):
    schedule = models.ForeignKey(
        Schedule,
        on_delete=models.CASCADE,
        verbose_name='스케줄'
    )
    first_category = models.CharField(
        max_length=5,
        verbose_name='상위 카테고리'
    )
    second_category = models.CharField(
        max_length=5,
        verbose_name='하위 카테고리'
    )
    content = models.CharField(
        max_length=100,
        verbose_name='부가정보'
    )

    class Meta:
        db_table = 'schedule_category'
        verbose_name = '스케줄 카테고리'
        verbose_name_plural = '스케줄 카테고리들'

    def __str__(self):
        return self.first_category
