# Generated by Django 3.2.3 on 2021-05-31 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210530_2103'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='room',
            field=models.CharField(default='0', max_length=1, verbose_name='Комната'),
        ),
    ]
