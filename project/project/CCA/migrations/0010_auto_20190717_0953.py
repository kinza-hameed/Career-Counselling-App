# Generated by Django 2.2.3 on 2019-07-17 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CCA', '0009_auto_20190717_0939'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_marks',
            name='Computer',
        ),
        migrations.RemoveField(
            model_name='user_marks',
            name='English',
        ),
        migrations.RemoveField(
            model_name='user_marks',
            name='Physics',
        ),
        migrations.AddField(
            model_name='user_marks',
            name='COMPUTER',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='user_marks',
            name='ENGLISH',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='user_marks',
            name='PHYSICS',
            field=models.IntegerField(default='0'),
        ),
    ]
