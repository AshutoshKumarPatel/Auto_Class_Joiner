# Generated by Django 4.1.4 on 2023-01-01 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TimeTable', '0004_time_table_delete_monday'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Time_Table',
            new_name='TimeTable',
        ),
    ]
