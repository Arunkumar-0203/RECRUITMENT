# Generated by Django 3.2.12 on 2022-04-21 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RECRUITMENT_APP', '0025_one_to_one'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group_discussion',
            name='date',
            field=models.DateField(max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='group_discussion',
            name='time',
            field=models.TimeField(max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='one_to_one',
            name='date',
            field=models.DateField(max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='one_to_one',
            name='time',
            field=models.TimeField(max_length=400, null=True),
        ),
    ]