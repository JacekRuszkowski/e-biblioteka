# Generated by Django 3.1.1 on 2021-01-29 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default_profile.jpg', upload_to='profile_pics'),
        ),
    ]