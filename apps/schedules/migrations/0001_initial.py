# Generated by Django 2.0.4 on 2018-04-10 23:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('celebritys', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='스케줄명')),
                ('schedule', models.DateTimeField(verbose_name='일정')),
                ('celebrity', models.ManyToManyField(to='celebritys.Celebrity', verbose_name='출연 셀럽')),
            ],
            options={
                'verbose_name': '스케줄',
                'verbose_name_plural': '스케줄들',
                'db_table': 'schedule',
            },
        ),
        migrations.CreateModel(
            name='ScheduleCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_category', models.CharField(max_length=5, verbose_name='상위 카테고리')),
                ('second_category', models.CharField(max_length=5, verbose_name='하위 카테고리')),
                ('content', models.CharField(max_length=100, verbose_name='부가정보')),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedules.Schedule', verbose_name='스케줄')),
            ],
            options={
                'verbose_name': '스케줄 카테고리',
                'verbose_name_plural': '스케줄 카테고리들',
                'db_table': 'schedule_category',
            },
        ),
    ]
