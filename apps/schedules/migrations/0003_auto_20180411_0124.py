# Generated by Django 2.0.4 on 2018-04-11 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0002_auto_20180411_0119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedulecategory',
            name='content',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='부가정보'),
        ),
        migrations.AlterField(
            model_name='schedulecategory',
            name='second_category',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='하위 카테고리'),
        ),
    ]
