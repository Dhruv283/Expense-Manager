# Generated by Django 2.2.4 on 2019-10-17 04:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('splits', '0004_auto_20191017_1008'),
    ]

    operations = [
        migrations.CreateModel(
            name='friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frnd', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='splits.person')),
            ],
        ),
        migrations.CreateModel(
            name='f_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frnd', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='splits.friend')),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='splits.person')),
            ],
        ),
    ]
