# Generated by Django 2.0.4 on 2018-04-10 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celebritys', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='celebrity',
            name='entertainment',
            field=models.ManyToManyField(blank=True, to='entertainments.Entertainment', verbose_name='소속사'),
        ),
    ]