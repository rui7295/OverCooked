# Generated by Django 2.0.4 on 2018-05-14 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foreground', '0006_auto_20180514_1111'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]