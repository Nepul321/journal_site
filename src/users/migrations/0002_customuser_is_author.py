# Generated by Django 4.2.5 on 2023-10-28 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_author',
            field=models.BooleanField(default=False),
        ),
    ]
