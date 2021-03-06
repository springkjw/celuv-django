# Generated by Django 2.0.4 on 2018-04-10 23:11

import apps.entertainments.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('celebritys', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Entertainment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='기획사명')),
                ('image', models.ImageField(blank=True, null=True, upload_to=apps.entertainments.models.entertainment_image, verbose_name='사진')),
                ('start', models.DateField(blank=True, null=True, verbose_name='설립일')),
                ('homepage', models.URLField(blank=True, null=True, verbose_name='홈페이지')),
                ('code', models.CharField(blank=True, max_length=100, null=True, verbose_name='가입코드')),
            ],
            options={
                'verbose_name': '기획사',
                'verbose_name_plural': '기획사들',
                'db_table': 'entertainment',
            },
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manager_type', models.CharField(choices=[('s', 'Super'), ('n', 'Normal')], default='n', max_length=10, verbose_name='권한')),
                ('position', models.CharField(blank=True, max_length=50, null=True, verbose_name='직책')),
                ('celebrity', models.ManyToManyField(blank=True, to='celebritys.Celebrity', verbose_name='연예인')),
                ('entertainment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='manager', to='entertainments.Entertainment', verbose_name='기획사')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='manager_user', to=settings.AUTH_USER_MODEL, verbose_name='유저')),
            ],
            options={
                'verbose_name': '기획사 매니저',
                'verbose_name_plural': '기획서 매니저들',
                'db_table': 'entertainment_manager',
            },
        ),
    ]
