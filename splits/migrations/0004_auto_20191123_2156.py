# Generated by Django 2.1.5 on 2019-11-23 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('splits', '0003_expense_amt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='youareowed',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='account',
            name='youowe',
            field=models.FloatField(default=0),
        ),
    ]
