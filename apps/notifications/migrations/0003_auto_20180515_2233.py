# Generated by Django 2.0.4 on 2018-05-15 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0002_auto_20180515_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='notification_type',
            field=models.CharField(choices=[('c', '연예인'), ('s', '스케줄')], default='c', max_length=1, verbose_name='알림 유형'),
        ),
    ]
