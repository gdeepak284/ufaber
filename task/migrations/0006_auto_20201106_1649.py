# Generated by Django 3.0.6 on 2020-11-06 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0005_subtask'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='end_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='task',
            name='start_date',
            field=models.DateTimeField(),
        ),
    ]
