# Generated by Django 3.2.12 on 2022-04-19 04:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('RECRUITMENT_APP', '0013_auto_20220419_1016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='company',
        ),
        migrations.AlterField(
            model_name='feedback',
            name='USER',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
