

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('VisaRegistration', '0006_auto_20211118_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visa',
            name='number_visa',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
