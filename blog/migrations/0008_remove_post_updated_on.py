# Generated by Django 4.2.16 on 2024-11-25 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_vote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='updated_on',
        ),
    ]
