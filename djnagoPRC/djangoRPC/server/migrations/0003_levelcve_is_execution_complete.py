# Generated by Django 4.2.5 on 2023-11-30 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0002_scaninfo_is_execution_complete'),
    ]

    operations = [
        migrations.AddField(
            model_name='levelcve',
            name='is_execution_complete',
            field=models.BooleanField(default=False),
        ),
    ]
