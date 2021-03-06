# Generated by Django 3.0.5 on 2020-04-28 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uni_ticket', '0094_auto_20200424_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketcategoryinputlist',
            name='field_type',
            field=models.CharField(choices=[('CustomFileField', 'Allegato (generico)'), ('CustomImageField', 'Allegato Immagine'), ('CustomSignedP7MField', 'Allegato P7M firmato'), ('CustomPDFField', 'Allegato PDF'), ('CustomSignedPdfField', 'Allegato PDF firmato'), ('CustomDataField', 'Allegato file dati (JSON, CSV, Excel)'), ('CaptchaHiddenField', 'Campo nascosto'), ('CustomHiddenField', 'Campo nascosto'), ('CustomCaptchaComplexField', 'Captcha'), ('CheckBoxField', 'Checkbox'), ('MultiCheckBoxField', 'Checkbox multi-valore'), ('BaseDateField', 'Data'), ('BaseDateTimeField', 'Data e Ora'), ('DateStartEndComplexField', 'Data inizio e Data fine'), ('CustomEmailField', 'E-mail'), ('CustomComplexTableField', 'Inserimenti multipli'), ('CustomRadioBoxField', 'Lista di opzioni (checkbox)'), ('CustomSelectBoxField', 'Lista di opzioni (tendina)'), ('PositiveFloatField', 'Numero con virgola positivo'), ('PositiveIntegerField', 'Numero intero positivo'), ('ProtocolloField', 'Protocollo (tipo/numero/data)'), ('CustomCharField', 'Testo'), ('TextAreaField', 'Testo lungo')], max_length=100),
        ),
    ]
