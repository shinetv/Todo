# Generated by Django 3.2.3 on 2021-12-13 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ToDo', '0002_user_task'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='user_task',
            new_name='tasks',
        ),
    ]
