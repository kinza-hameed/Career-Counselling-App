# Generated by Django 2.2.3 on 2019-07-03 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CCA', '0005_auto_20190703_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='difficulty_level',
            name='ID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='field',
            name='ID1',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
