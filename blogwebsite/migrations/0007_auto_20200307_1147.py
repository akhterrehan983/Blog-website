# Generated by Django 3.0.3 on 2020-03-07 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogwebsite', '0006_auto_20200307_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(default='images/blankprofile.webp', upload_to='images'),
        ),
    ]
