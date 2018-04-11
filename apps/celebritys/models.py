from django.db import models
from django.conf import settings
from django.urls import reverse_lazy

from apps.entertainments.models import Entertainment


def celebrity_image(instance, filename):
    return 'celebrity/%s/%s' % (instance.pk, filename)


class Celebrity(models.Model):
    CELEB_TYPE = (
        ('g', '그룹/팀'),
        ('s', '개인'),
    )
    SEX_TYPE = (
        ('m', '남자'),
        ('f', '여자'),
    )

    name = models.CharField(
        max_length=50,
        verbose_name='셀럽명'
    )
    image = models.ImageField(
        null=True,
        blank=True,
        upload_to=celebrity_image,
        verbose_name='연예인 사진'
    )
    celeb_type = models.CharField(
        max_length=2,
        default='s',
        choices=CELEB_TYPE,
        verbose_name='유형'
    )
    entertainment = models.ManyToManyField(
        Entertainment,
        blank=True,
        verbose_name='소속사'
    )
    debut = models.DateField(
        null=True,
        blank=True,
        verbose_name='데뷔일'
    )
    real_name = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        verbose_name='본명'
    )
    birth = models.DateField(
        null=True,
        blank=True,
        verbose_name='생일'
    )
    sex = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        choices=SEX_TYPE,
        verbose_name='성별'
    )
    like = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
        verbose_name='찜하기'
    )

    class Meta:
        db_table = 'celebrity'
        verbose_name = '연예인'
        verbose_name_plural = '연예인들'

    def __str__(self):
        return self.name

    @property
    def get_profile_image(self):
        if not self.image:
            return settings.STATIC_URL + '/img/empty_profile.svg'
        return self.image.url

    @property
    def get_update_url(self):
        return reverse_lazy('celebrity:update', kwargs={'pk': self.pk})
