# Generated by Django 2.0.4 on 2018-05-15 12:41

import apps.feedbacks.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feedbacks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='시간')),
                ('image_url', models.ImageField(upload_to=apps.feedbacks.models.report_image, verbose_name='제보')),
            ],
            options={
                'verbose_name': '제보 이미지',
                'verbose_name_plural': '제보 이미지들',
                'db_table': 'report_image',
            },
        ),
        migrations.AlterField(
            model_name='report',
            name='url',
            field=models.CharField(blank=True, max_length=500, verbose_name='제보 관련 url'),
        ),
        migrations.AddField(
            model_name='reportimage',
            name='report',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='feedbacks.Report', verbose_name='제보'),
        ),
    ]
