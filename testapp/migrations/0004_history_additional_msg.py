# Generated by Django 3.0.3 on 2021-01-31 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0003_auto_20210131_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='additional_msg',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]