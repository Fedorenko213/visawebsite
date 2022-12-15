

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VisaRegistration', '0012_alter_visa_number_visa'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visa',
            old_name='number_visa',
            new_name='code_visa',
        ),
    ]
