# Generated by Django 2.2.2 on 2019-06-24 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_movie_video_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='video_name',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='videofile',
        ),
        migrations.AddField(
            model_name='movie',
            name='video_id',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
    ]
