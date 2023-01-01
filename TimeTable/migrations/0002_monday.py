# Generated by Django 4.1.4 on 2022-12-31 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TimeTable', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Monday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('class_image', models.ImageField(upload_to='Class_Images')),
                ('record_class', models.BooleanField(default=0)),
                ('save_screenshot', models.BooleanField(default=0)),
                ('timing', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='TimeTable.timings')),
            ],
        ),
    ]