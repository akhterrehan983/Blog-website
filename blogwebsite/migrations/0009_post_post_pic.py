# Generated by Django 3.0.3 on 2020-03-07 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogwebsite', '0008_auto_20200307_1215'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_pic',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
