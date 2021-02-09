# Generated by Django 3.1.1 on 2021-02-04 14:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('wypozyczalnia', '0017_auto_20210204_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='return_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 18, 14, 57, 9, 704096, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(choices=[(1, '1 - Bardzo słaba'), (2, '2 - Słaba'), (3, '3 - Średnia'), (4, '4 - Dobra'), (5, '5 - Bardzo dobra')], default=1),
        ),
    ]
