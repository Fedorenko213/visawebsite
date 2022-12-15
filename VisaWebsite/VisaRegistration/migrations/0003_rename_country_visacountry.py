

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VisaRegistration', '0002_country_visa_visastatus_visatariff_visatype'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Country',
            new_name='VisaCountry',
        ),
    ]
