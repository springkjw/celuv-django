# Generated by Django 2.0.4 on 2018-04-11 00:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('celebritys', '0002_celebrity_entertainment'),
    ]

    operations = [
        migrations.AddField(
            model_name='celebrity',
            name='like',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='찜하기'),
        ),
    ]