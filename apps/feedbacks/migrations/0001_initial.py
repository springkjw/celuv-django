# Generated by Django 2.0.4 on 2018-04-24 14:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, choices=[('cs001', '불편사항 신고'), ('cs002', '서비스 개선 제안'), ('cs003', '서비스 문의'), ('cs004', '저작권/권리 침해'), ('cs005', '기타')], max_length=5, verbose_name='카테고리')),
                ('content', models.TextField(blank=True, verbose_name='의견 내용')),
                ('timestamp', models.DateTimeField(auto_now=True, verbose_name='신청 날짜')),
                ('is_confirm', models.BooleanField(default=False, verbose_name='확인 여부')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='유저')),
            ],
            options={
                'verbose_name': '피드백',
                'verbose_name_plural': '피드백들',
                'db_table': 'feedback',
            },
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('celebrity', models.CharField(blank=True, max_length=255, verbose_name='제보할 연예인')),
                ('url', models.CharField(blank=True, max_length=255, verbose_name='제보 관련 url')),
                ('timestamp', models.DateTimeField(auto_now=True, verbose_name='신청 날짜')),
                ('is_confirm', models.BooleanField(default=False, verbose_name='확인 여부')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='유저')),
            ],
            options={
                'verbose_name': '제보',
                'verbose_name_plural': '제보들',
                'db_table': 'report',
            },
        ),
    ]