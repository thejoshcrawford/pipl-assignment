# Generated by Django 2.2.4 on 2019-08-24 04:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls_api', '0007_pollresponse_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BrowserInstance',
        ),
    ]
