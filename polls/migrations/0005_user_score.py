# Generated by Django 4.0.6 on 2022-07-13 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='score',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
