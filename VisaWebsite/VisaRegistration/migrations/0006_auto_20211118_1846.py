

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VisaRegistration', '0005_auto_20211118_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visa',
            name='payment_amount',
            field=models.DecimalField(blank=True, decimal_places=4, help_text='Заповнюється автоматично по полю з вибраного тарифу', max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='visa',
            name='valid_date',
            field=models.DateField(blank=True, help_text='Заповнюється автоматично по полю з вибраного тарифу', null=True),
        ),
    ]
