# Generated by Django 2.2.3 on 2019-07-03 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CCA', '0004_auto_20190703_1557'),
    ]

    operations = [
        migrations.RenameField(
            model_name='difficulty_level',
            old_name='levels',
            new_name='marks',
        ),
        migrations.AddField(
            model_name='difficulty_level',
            name='diff_levels',
            field=models.CharField(default=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='difficulty_level',
            name='ID',
            field=models.AutoField(default=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='field',
            name='ID1',
            field=models.AutoField(default=True, primary_key=True, serialize=False),
        ),
    ]
