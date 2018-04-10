import uuid
import json

from django.db import models
from django.conf import settings
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class MyUserQuerySet(models.QuerySet):
    def user(self):
        return self.filter(is_manager=False, is_admin=False)

    def manager(self):
        return self.filter(is_manager=True, is_admin=False)

    def admin(self):
        return self.filter(is_manager=True, is_admin=True)


class MyUserManager(BaseUserManager):
    def get_queryset(self):
        return MyUserQuerySet(self.model, using=self._db)

    def _create_user(self, email, password, **kwargs):
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **kwargs):
        return self._create_user(email, password, **kwargs)

    def create_manager(self, email, password, **kwargs):
        kwargs.setdefault('is_manager', True)
        return self._create_user(email, password, **kwargs)

    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault('is_admin', True)
        return self._create_user(email, password, **kwargs)

    def user(self):
        return self.get_queryset().user()

    def manager(self):
        return self.get_queryset().manager()

    def admin(self):
        return self.get_queryset().admin()


def user_profile_image(instance, filename):
    return "%s/%s" % (instance.id, filename)


class MyUser(AbstractBaseUser):
    # 유저 모델
    SEX = (
        ('f', '여자'),
        ('m', '남자'),
    )
    PROVIDER = (
        ('celuv', '셀럽'),
        ('facebook', '페이스북'),
        ('kakao', '카카오'),
        ('google', '구글'),
    )

    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        auto_created=True,
        unique=True,
        verbose_name="pk"
    )
    email = models.EmailField(
        unique=True,
        verbose_name='이메일'
    )
    provider = models.CharField(
        max_length=1,
        choices=PROVIDER,
        default='c',
        verbose_name='가입경로'
    )
    uid = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='소셜로그인 키',
        help_text='소셜로그인인 경우만'
    )
    name = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        verbose_name='이름'
    )
    image = models.ImageField(
        upload_to=user_profile_image,
        null=True,
        blank=True,
        verbose_name='프로필 이미지'
    )
    sex = models.CharField(
        max_length=1,
        choices=SEX,
        null=True,
        blank=True,
        verbose_name='성별'
    )
    birth = models.DateField(
        null=True,
        blank=True,
        verbose_name='생일'
    )
    phone = models.CharField(
        max_length=14,
        null=True,
        blank=True,
        verbose_name='연락처'
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
        verbose_name='가입일'
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name='활성화 여부'
    )
    is_manager = models.BooleanField(
        default=False,
        verbose_name='매니저 여부'
    )
    is_admin = models.BooleanField(
        default=False,
        verbose_name='관리자 여부'
    )

    objects = MyUserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        db_table = 'user'
        verbose_name = '유저'
        verbose_name_plural = '유저들'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    @property
    def get_profile_image(self):
        if not self.image:
            return None
        return self.image.url

    @property
    def get_report_count(self):
        return 0

    @property
    def get_feedback_count(self):
        return 0

    @property
    def get_celeb_count(self):
        return 0
