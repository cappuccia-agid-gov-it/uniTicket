# Generated by Django 3.0.6 on 2020-06-11 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uni_ticket', '0120_auto_20200601_2347'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ticketcategory',
            options={'ordering': ['name'], 'verbose_name': 'Categoria della Richiesta', 'verbose_name_plural': 'Categorie delle Richieste'},
        ),
        migrations.AlterModelOptions(
            name='ticketcategorymodule',
            options={'ordering': ['-created'], 'verbose_name': 'Modulo di Inserimento Richiesta', 'verbose_name_plural': 'Moduli di Inserimento Richieste'},
        ),
        migrations.AlterField(
            model_name='ticketcategory',
            name='confirm_message_text',
            field=models.TextField(blank=True, help_text='Es: \'Hai correttamente confermato la tua partecipazione\'. Apri e chiudi le parentesi graffe per inserire l\'oggetto della richiesta. Lascia vuoto per usare il testo predefinito "Richiesta "{}" creata con successo"', max_length=500, null=True, verbose_name='Messaggio di conferma'),
        ),
        migrations.AlterField(
            model_name='ticketcategory',
            name='is_active',
            field=models.BooleanField(default=False, help_text='Se disabilitato, non sarà visibile in Aggiungi Richiesta'),
        ),
        migrations.AlterField(
            model_name='ticketcategory',
            name='is_notify',
            field=models.BooleanField(default=False, help_text='Richiesta che viene automaticamente presa in carico', verbose_name='Richiesta di tipo Notifica'),
        ),
        migrations.AlterField(
            model_name='ticketcategory',
            name='receive_email',
            field=models.BooleanField(default=False, help_text='Invia email a operatori per ogni richiesta aperta', verbose_name='Mail ad operatori'),
        ),
        migrations.AlterField(
            model_name='ticketcategory',
            name='show_heading_text',
            field=models.BooleanField(default=True, verbose_name='Mostra agli utenti un testo di accettazione in fase di apertura nuova richiesta'),
        ),
    ]
