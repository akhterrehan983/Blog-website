# Generated by Django 3.0.3 on 2020-03-07 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogwebsite', '0004_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
