# Generated by Django 2.0.6 on 2018-12-08 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0012_event_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='event_images'),
        ),
    ]