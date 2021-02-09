# Generated by Django 3.1.1 on 2021-01-22 17:33

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wypozyczalnia', '0009_orderitem_return_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='return_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 5, 17, 33, 4, 972930, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_content', models.TextField()),
                ('rating', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)])),
                ('review_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('review_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('review_book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wypozyczalnia.book')),
            ],
        ),
    ]
