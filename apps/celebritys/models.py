from django.db import models
from django.conf import settings


def celebrity_profile_image(instance, filename):
    return '%s/%s' % (instance.pk, filename)


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
        upload_to=celebrity_profile_image,
        verbose_name='연예인 사진'
    )
    celeb_type = models.CharField(
        max_length=2,
        default='s',
        choices=CELEB_TYPE,
        verbose_name='유형'
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
