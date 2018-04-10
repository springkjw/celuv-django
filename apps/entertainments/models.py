from django.db import models
from django.conf import settings


def entertainment_image(instance, filename):
    return "entertainment/%s/%s" % (instance.pk, filename)


class Entertainment(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='기획사명'
    )
    image = models.ImageField(
        null=True,
        blank=True,
        upload_to=entertainment_image,
        verbose_name='사진'
    )
    start = models.DateField(
        null=True,
        blank=True,
        verbose_name='설립일'
    )
    homepage = models.URLField(
        null=True,
        blank=True,
        verbose_name='홈페이지'
    )
    code = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='가입코드'
    )

    class Meta:
        db_table = 'entertainment'
        verbose_name = '기획사'
        verbose_name_plural = '기획사들'

    def __str__(self):
        return self.name

    @property
    def get_profile_image(self):
        if not self.image:
            return settings.STATIC_URL + '/img/empty_profile.svg'
        return self.image.url

    @property
    def get_celeb_count(self):
        return self.entertainment.count()


class Manager(models.Model):
    # 엔터테인먼트 매니저
    POSITION = (
        ('s', 'Super'),
        ('n', 'Normal'),
    )
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='manager_user',
        verbose_name='유저'
    )
    entertainment = models.ForeignKey(
        Entertainment,
        on_delete=models.CASCADE,
        related_name='manager',
        verbose_name='기획사'
    )
    celebrity = models.ManyToManyField(
        'celebritys.Celebrity',
        blank=True,
        verbose_name='연예인'
    )
    manager_type = models.CharField(
        max_length=10,
        choices=POSITION,
        default='n',
        verbose_name='권한'
    )
    position = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        verbose_name='직책'
    )

    class Meta:
        db_table = 'entertainment_manager'
        verbose_name = '기획사 매니저'
        verbose_name_plural = '기획서 매니저들'

    def __str__(self):
        return self.user.name
