# Generated by Django 5.1.3 on 2024-11-15 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_employee_position_alter_employee_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
    ]
