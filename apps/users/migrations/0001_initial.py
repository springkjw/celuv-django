# Generated by Django 2.0.4 on 2018-04-10 23:11

import apps.users.models
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('uuid', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='pk')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='이메일')),
                ('provider', models.CharField(choices=[('celuv', '셀럽'), ('facebook', '페이스북'), ('kakao', '카카오'), ('google', '구글')], default='c', max_length=1, verbose_name='가입경로')),
                ('uid', models.CharField(blank=True, help_text='소셜로그인인 경우만', max_length=255, null=True, verbose_name='소셜로그인 키')),
                ('name', models.CharField(blank=True, max_length=20, null=True, verbose_name='이름')),
                ('image', models.ImageField(blank=True, null=True, upload_to=apps.users.models.user_profile_image, verbose_name='프로필 이미지')),
                ('sex', models.CharField(blank=True, choices=[('f', '여자'), ('m', '남자')], max_length=1, null=True, verbose_name='성별')),
                ('birth', models.DateField(blank=True, null=True, verbose_name='생일')),
                ('phone', models.CharField(blank=True, max_length=14, null=True, verbose_name='연락처')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='가입일')),
                ('is_active', models.BooleanField(default=True, verbose_name='활성화 여부')),
                ('is_manager', models.BooleanField(default=False, verbose_name='매니저 여부')),
                ('is_admin', models.BooleanField(default=False, verbose_name='관리자 여부')),
            ],
            options={
                'verbose_name': '유저',
                'verbose_name_plural': '유저들',
                'db_table': 'user',
            },
        ),
    ]
