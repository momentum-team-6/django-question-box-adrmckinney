# Generated by Django 3.1.4 on 2021-01-08 00:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_answers_questions'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Answers',
            new_name='Answer',
        ),
        migrations.RenameModel(
            old_name='Questions',
            new_name='Question',
        ),
    ]