# Generated by Django 4.1.3 on 2022-12-06 10:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_alter_audio_date_created'),
    ]

    operations = [
        migrations.RenameField(
            model_name='audio',
            old_name='name',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='audio',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 6, 10, 49, 21, 752030, tzinfo=datetime.timezone.utc)),
        ),
    ]
