# Generated by Django 3.2.12 on 2022-04-19 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RECRUITMENT_APP', '0016_aptitude_questions_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='aptitude_questions',
            name='status',
            field=models.CharField(default='test', max_length=400),
        ),
    ]