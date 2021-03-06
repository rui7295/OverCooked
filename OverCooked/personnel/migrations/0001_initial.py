# Generated by Django 2.0.4 on 2018-05-14 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Distribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('phone', models.CharField(max_length=4)),
                ('performance', models.IntegerField(null=True)),
                ('salary', models.DecimalField(blank=True, decimal_places=2, max_digits=16, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Salary',  # Job to Salary
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('salary', models.DecimalField(blank=True, decimal_places=2, max_digits=16, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='distribute',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personnel.Employee'),
        ),
        migrations.AddField(
            model_name='distribute',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personnel.Salary'),
        ),
    ]
