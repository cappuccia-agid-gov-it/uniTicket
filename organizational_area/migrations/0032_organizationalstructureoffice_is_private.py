# Generated by Django 3.1.2 on 2020-10-16 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizational_area', '0031_auto_20200702_1126'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizationalstructureoffice',
            name='is_private',
            field=models.BooleanField(default=False),
        ),
    ]
