# Generated by Django 5.1.4 on 2024-12-24 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='body',
            new_name='content',
        ),
    ]
