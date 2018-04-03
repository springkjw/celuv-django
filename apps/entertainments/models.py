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


# class Manager(models.Model);
#     # 엔터테인먼트 매니저
#     POSITION = (
#         ('', ''),
#         ('', ''),
#     )
#     user 
#     entertainment = 

#     class Meta:
#         db_tabe = 'entertainment_manager'
#         verbose_name = '기획사 매니저'
#         verbose_name_plural = '기획서 매니저들'

#     def __str__(self):
#         return self.