# Generated by Django 3.1.2 on 2021-02-15 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20210103_1213'),
    ]

    operations = [
        migrations.AddField(
            model_name='twitteraccount',
            name='following_num',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='twitteraccount',
            name='protected',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='twitteraccount',
            name='suspended',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='twitteraccount',
            name='twitter_id',
            field=models.TextField(default='123'),
            preserve_default=False,
        ),
    ]
