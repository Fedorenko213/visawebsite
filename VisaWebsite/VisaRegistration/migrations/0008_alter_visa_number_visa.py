

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VisaRegistration', '0007_alter_visa_number_visa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visa',
            name='number_visa',
            field=models.UUIDField(default='e5938a2cece4', editable=False, primary_key=True, serialize=False),
        ),
    ]
