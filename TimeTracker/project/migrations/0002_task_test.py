# Generated by Django 2.2.1 on 2019-07-25 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='test',
            field=models.CharField(default='hai', max_length=200),
        ),
    ]