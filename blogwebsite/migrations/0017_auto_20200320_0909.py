# Generated by Django 3.0.4 on 2020-03-20 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogwebsite', '0016_comment_post_commenter_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment_post',
            name='commenter_pic',
            field=models.URLField(blank=True),
        ),
    ]
