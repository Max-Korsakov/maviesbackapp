# Generated by Django 3.1.1 on 2020-09-17 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviemodel',
            name='budget',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='moviemodel',
            name='revenue',
            field=models.BigIntegerField(),
        ),
    ]
