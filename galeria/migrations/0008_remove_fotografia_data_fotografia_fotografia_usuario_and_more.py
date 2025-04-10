# Generated by Django 5.1.6 on 2025-03-22 18:15

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0007_merge_20250322_1413'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fotografia',
            name='data_fotografia',
        ),
        migrations.AddField(
            model_name='fotografia',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='fotografia',
            name='data_publicacao',
            field=models.DateTimeField(default=datetime.datetime(2025, 3, 22, 14, 15, 31, 271386)),
        ),
    ]
