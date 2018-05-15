from django.db import models
from django.conf import settings


class Feedback(models.Model):
    CATEGORY = (
        ('cs001', '불편사항 신고'),
        ('cs002', '서비스 개선 제안'),
        ('cs003', '서비스 문의'),
        ('cs004', '저작권/권리 침해'),
        ('cs005', '기타'),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name="유저"
    )
    category = models.CharField(
        max_length=5,
        choices=CATEGORY,
        blank=True,
        verbose_name="카테고리"
    )
    content = models.TextField(
        blank=True,
        verbose_name="의견 내용"
    )
    timestamp = models.DateTimeField(
        auto_now=True,
        verbose_name="신청 날짜"
    )
    is_confirm = models.BooleanField(
        default=False,
        verbose_name="확인 여부"
    )

    class Meta:
        db_table = 'feedback'
        verbose_name = '피드백'
        verbose_name_plural = '피드백들'


class Report(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="유저"
    )
    celebrity = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="제보할 연예인"
    )
    url = models.CharField(
        max_length=500,
        blank=True,
        verbose_name="제보 관련 url"
    )
    timestamp = models.DateTimeField(
        auto_now=True,
        verbose_name="신청 날짜"
    )
    is_confirm = models.BooleanField(
        default=False,
        verbose_name="확인 여부"
    )

    class Meta:
        db_table = 'report'
        verbose_name = "제보"
        verbose_name_plural = "제보들"


def report_image(instance, filename):
    return "report/%s/%s" % (
        instance.id,
        filename
    )


class ReportImage(models.Model):
    report = models.ForeignKey(
        Report,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='제보'
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='시간'
    )
    image_url = models.ImageField(
        upload_to=report_image,
        verbose_name='제보'
    )

    class Meta:
        db_table = 'report_image'
        verbose_name = '제보 이미지'
        verbose_name_plural = '제보 이미지들'

    def get_report_image(self):
        return str(self.image_url.url)
