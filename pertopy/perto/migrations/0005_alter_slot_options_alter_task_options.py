# Generated by Django 4.0 on 2023-03-08 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perto', '0004_remove_task_slots_slot_description_slot_status_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='slot',
            options={'ordering': ['title'], 'verbose_name': 'Slot', 'verbose_name_plural': 'Slots'},
        ),
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['title'], 'verbose_name': 'Task', 'verbose_name_plural': 'Tasks'},
        ),
    ]