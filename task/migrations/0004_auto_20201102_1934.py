# Generated by Django 3.0.6 on 2020-11-02 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_auto_20201102_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='avatar',
            field=models.ImageField(upload_to='images/'),
        ),
    ]