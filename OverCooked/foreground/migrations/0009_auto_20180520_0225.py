# Generated by Django 2.0.4 on 2018-05-19 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foreground', '0008_detail_station'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='station',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='kitchen.Station'),
        ),
    ]
