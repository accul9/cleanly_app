# Generated by Django 5.1.6 on 2025-03-04 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apiv1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='due_Date',
            new_name='due_date',
        ),
    ]
