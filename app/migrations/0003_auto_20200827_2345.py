# Generated by Django 3.1 on 2020-08-27 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200827_2032'),
    ]

    operations = [
        migrations.AddField(
            model_name='showmodel',
            name='Academic',
            field=models.CharField(default=True, max_length=30),
        ),
        migrations.AddField(
            model_name='showmodel',
            name='hack_befor',
            field=models.CharField(default=True, max_length=20),
        ),
        migrations.AddField(
            model_name='showmodel',
            name='hack_heard',
            field=models.CharField(default=True, max_length=30),
        ),
        migrations.AddField(
            model_name='showmodel',
            name='idea',
            field=models.TextField(default=True),
        ),
        migrations.AddField(
            model_name='showmodel',
            name='link',
            field=models.CharField(default=True, max_length=30),
        ),
        migrations.AddField(
            model_name='showmodel',
            name='problem',
            field=models.TextField(default=True),
        ),
        migrations.AddField(
            model_name='showmodel',
            name='team',
            field=models.CharField(default=True, max_length=20),
        ),
    ]
