# Generated by Django 2.0.6 on 2018-12-06 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0001_initial'),
        ('event', '0011_auto_20181202_2247'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='subject',
            field=models.ManyToManyField(to='subject.Subject'),
        ),
    ]