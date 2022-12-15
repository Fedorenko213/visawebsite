

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VisaRegistration', '0003_rename_country_visacountry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visa',
            name='payment_amount',
            field=models.DecimalField(decimal_places=4, max_digits=10, null=True),
        ),
    ]
