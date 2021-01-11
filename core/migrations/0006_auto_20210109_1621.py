# Generated by Django 3.1.4 on 2021-01-09 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20210108_0443'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='answer',
            name='is_correct',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='answer',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='question_body',
            field=models.TextField(),
        ),
    ]