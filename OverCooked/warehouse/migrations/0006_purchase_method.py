# Generated by Django 2.0.4 on 2018-06-01 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0005_purchase_term'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='method',
            field=models.CharField(max_length=16, null=True),
        ),
    ]
