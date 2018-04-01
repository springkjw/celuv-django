from django.db import models


def entertainment_image(self):
    return


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
