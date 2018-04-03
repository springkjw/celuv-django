# Generated by Django 2.0.4 on 2018-04-03 08:33

import apps.users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20180403_0808'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=apps.users.models.user_profile_image, verbose_name='프로필 이미지'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='oauth_key',
            field=models.CharField(blank=True, help_text='소셜로그인인 경우만', max_length=255, null=True, verbose_name='소셜로그인 키'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='provider',
            field=models.CharField(choices=[('c', '셀럽'), ('f', '페이스북'), ('k', '카카오'), ('g', '구글')], default='c', max_length=1, verbose_name='가입경로'),
        ),
    ]