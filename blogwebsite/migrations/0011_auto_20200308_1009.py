# Generated by Django 3.0.3 on 2020-03-08 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogwebsite', '0010_auto_20200308_0830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_pic',
            field=models.URLField(blank=True),
        ),
    ]
