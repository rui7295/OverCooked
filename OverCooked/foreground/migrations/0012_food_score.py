# Generated by Django 2.0.4 on 2018-05-27 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foreground', '0011_auto_20180527_1507'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]