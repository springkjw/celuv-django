# Generated by Django 2.0.4 on 2018-04-10 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entertainments', '0002_manager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='entertainment',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='entertainments.Entertainment', verbose_name='기획사'),
        ),
    ]
