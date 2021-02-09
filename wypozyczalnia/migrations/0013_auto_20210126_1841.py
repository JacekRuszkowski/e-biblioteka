# Generated by Django 3.1.3 on 2021-01-26 17:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('wypozyczalnia', '0012_auto_20210126_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='return_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 9, 17, 41, 13, 424129, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(default=1),
        ),
    ]
