# Generated by Django 4.2.5 on 2024-03-21 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0003_alter_dataserver_port'),
    ]

    operations = [
        migrations.AlterField(
            model_name='segmentresult',
            name='full_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='segmentresult',
            name='osfamily',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='segmentresult',
            name='osgen',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='segmentresult',
            name='vendor',
            field=models.CharField(max_length=100),
        ),
    ]
