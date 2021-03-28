# Generated by Django 3.1.7 on 2021-03-26 08:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrasi', '0002_auto_20210326_0828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='buy_price',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(99)]),
        ),
    ]