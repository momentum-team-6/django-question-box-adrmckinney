# Generated by Django 3.1.4 on 2021-01-10 06:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20210109_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
