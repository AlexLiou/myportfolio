# Generated by Django 3.0.6 on 2020-07-01 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='github',
            field=models.URLField(default='https://github.com/alexliou'),
        ),
        migrations.AddField(
            model_name='job',
            name='title',
            field=models.CharField(default='N/A', max_length=100),
        ),
    ]
