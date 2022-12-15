

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VisaRegistration', '0004_alter_visa_payment_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visa',
            name='payment_amount',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='visa',
            name='valid_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
