# Generated by Django 4.2.1 on 2023-09-22 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientBD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_client', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ScanInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_status', models.CharField(max_length=20)),
                ('protocols', models.CharField(max_length=20)),
                ('open_ports', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('data_chunk', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SegmentScan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=20)),
                ('mask', models.CharField(max_length=20)),
                ('mode', models.CharField(max_length=20)),
                ('state_scan', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='DataServer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(default=False, max_length=10)),
                ('ip', models.CharField(max_length=20)),
                ('port', models.CharField(max_length=20)),
                ('mode', models.CharField(max_length=20)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='server.clientbd')),
            ],
        ),
    ]
