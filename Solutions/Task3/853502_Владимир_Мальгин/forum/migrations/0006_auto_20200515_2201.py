# Generated by Django 3.0.5 on 2020-05-15 19:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0005_auto_20200515_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 15, 22, 1, 29, 278332)),
        ),
        migrations.AlterField(
            model_name='message',
            name='text',
            field=models.TextField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='theme',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 15, 22, 1, 29, 278332)),
        ),
        migrations.AlterField(
            model_name='theme',
            name='description',
            field=models.TextField(default='', max_length=1024),
        ),
        migrations.AlterField(
            model_name='topic',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 15, 22, 1, 29, 277335)),
        ),
    ]
