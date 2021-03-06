# Generated by Django 3.2.12 on 2022-04-06 05:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('RECRUITMENT_APP', '0010_auto_20220405_1146'),
    ]

    operations = [
        migrations.CreateModel(
            name='application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='null', max_length=100, null=True)),
                ('aptitude', models.CharField(default='null', max_length=100, null=True)),
                ('gd', models.CharField(default='null', max_length=100, null=True)),
                ('one_TO_one', models.CharField(default='null', max_length=100, null=True)),
                ('final_status', models.CharField(default='null', max_length=100, null=True)),
                ('requirement', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='RECRUITMENT_APP.requirement')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
