# Generated by Django 4.1.4 on 2023-01-01 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TimeTable', '0006_monday_tuesday_delete_timetable'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=9)),
                ('subject', models.CharField(max_length=255)),
                ('class_image', models.ImageField(upload_to='Class_Images')),
                ('record_class', models.BooleanField(default=False)),
                ('save_screenshot', models.BooleanField(default=False)),
                ('timing', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='TimeTable.timing')),
            ],
        ),
        migrations.RemoveField(
            model_name='tuesday',
            name='timing',
        ),
        migrations.DeleteModel(
            name='Monday',
        ),
        migrations.DeleteModel(
            name='Tuesday',
        ),
    ]
