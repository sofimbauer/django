# Generated by Django 5.0.1 on 2024-03-10 02:04

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DatosExtra',
            new_name='DatosExtras',
        ),
    ]
