# Generated by Django 3.0.5 on 2020-04-28 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uni_ticket', '0095_auto_20200428_1303'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ticketcategoryinputlist',
            options={'ordering': ['ordinamento'], 'verbose_name': 'Modulo di inserimento', 'verbose_name_plural': 'Moduli di inserimento'},
        ),
    ]
