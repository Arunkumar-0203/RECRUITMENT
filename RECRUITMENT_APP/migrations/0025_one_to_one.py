# Generated by Django 3.2.12 on 2022-04-21 05:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RECRUITMENT_APP', '0024_remove_group_discussion_status1'),
    ]

    operations = [
        migrations.CreateModel(
            name='one_to_one',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=400, null=True)),
                ('date', models.CharField(max_length=400, null=True)),
                ('link', models.URLField(default='test', max_length=400, null=True)),
                ('status', models.CharField(default='test', max_length=400)),
                ('USER', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='RECRUITMENT_APP.user')),
                ('form', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='RECRUITMENT_APP.application')),
            ],
        ),
    ]
