# Generated by Django 4.2.1 on 2023-05-13 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='created',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='todo',
            old_name='updated',
            new_name='updated_date',
        ),
    ]
