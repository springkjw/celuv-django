# Generated by Django 2.0.4 on 2018-04-11 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedulecategory',
            name='first_category',
            field=models.CharField(choices=[('r', '라디오 스케줄'), ('t', '티비 스케줄'), ('c', '공연행사'), ('a', '앨범발매'), ('p', '촬영'), ('f', '팬미팅'), ('e', '기타')], default='t', max_length=5, verbose_name='상위 카테고리'),
        ),
    ]