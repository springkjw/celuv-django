# Generated by Django 2.0.4 on 2018-04-03 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20180403_0804'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='myuser',
            options={'verbose_name': '유저', 'verbose_name_plural': '유저들'},
        ),
    ]
