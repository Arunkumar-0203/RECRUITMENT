# Generated by Django 3.2.12 on 2022-05-06 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RECRUITMENT_APP', '0031_guest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guest',
            name='photo',
        ),
    ]
