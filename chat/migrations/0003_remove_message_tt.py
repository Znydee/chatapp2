# Generated by Django 4.0.6 on 2022-08-25 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_message_tt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='tt',
        ),
    ]