# Generated by Django 5.0.6 on 2024-05-11 04:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='create_at',
            new_name='created_at',
        ),
    ]
