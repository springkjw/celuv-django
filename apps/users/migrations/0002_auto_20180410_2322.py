# Generated by Django 2.0.4 on 2018-04-10 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='provider',
            field=models.CharField(choices=[('celuv', '셀럽'), ('facebook', '페이스북'), ('kakao', '카카오'), ('google', '구글')], default='c', max_length=10, verbose_name='가입경로'),
        ),
    ]
