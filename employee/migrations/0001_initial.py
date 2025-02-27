# Generated by Django 5.1.3 on 2024-11-15 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('age', models.PositiveIntegerField()),
                ('phone_no', models.PositiveIntegerField()),
                ('department', models.CharField(max_length=100)),
                ('salary', models.PositiveIntegerField()),
            ],
        ),
    ]
