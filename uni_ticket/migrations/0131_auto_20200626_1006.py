# Generated by Django 3.0.7 on 2020-06-26 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uni_ticket', '0130_auto_20200623_0927'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizationalstructurewsarchipro',
            name='protocollo_email',
            field=models.CharField(default='amministrazione@pec.unical.it', max_length=255, verbose_name='E-mail'),
        ),
        migrations.AddField(
            model_name='ticketcategorywsarchipro',
            name='protocollo_email',
            field=models.CharField(default='amministrazione@pec.unical.it', max_length=255, verbose_name='E-mail'),
        ),
    ]