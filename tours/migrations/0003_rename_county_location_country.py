# Generated by Django 3.2.16 on 2024-10-08 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0002_auto_20241008_1246'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='county',
            new_name='country',
        ),
    ]