# Generated by Django 3.0.5 on 2020-05-15 14:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='topic',
            new_name='theme',
        ),
        migrations.AddField(
            model_name='message',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 15, 17, 45, 46, 510819)),
        ),
        migrations.AddField(
            model_name='theme',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 15, 17, 45, 46, 510819)),
        ),
        migrations.AddField(
            model_name='topic',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 15, 17, 45, 46, 509823)),
        ),
    ]
