

from django.db import migrations, models
import shortuuidfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('VisaRegistration', '0009_alter_visa_number_visa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visa',
            name='number_visa',
            field=models.CharField(default=shortuuidfield.fields.ShortUUIDField, editable=False, help_text='User UUID', max_length=22, primary_key=True, serialize=False),
        ),
    ]
