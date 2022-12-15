

import VisaRegistration.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('VisaRegistration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('country_code', models.IntegerField(primary_key=True, serialize=False)),
                ('country', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Країни віз',
                'verbose_name_plural': 'Країни віз',
            },
        ),
        migrations.CreateModel(
            name='VisaStatus',
            fields=[
                ('status_code', models.IntegerField(primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Статусы віз',
                'verbose_name_plural': 'Статусы віз',
            },
        ),
        migrations.CreateModel(
            name='VisaTariff',
            fields=[
                ('tariff_number', models.IntegerField(primary_key=True, serialize=False)),
                ('validity_period', models.DecimalField(decimal_places=0, max_digits=10, null=True)),
                ('coefficient', models.DecimalField(decimal_places=4, max_digits=10, null=True)),
                ('payment_amount', models.DecimalField(decimal_places=4, max_digits=10, null=True)),
            ],
            options={
                'verbose_name': 'Термін віз',
                'verbose_name_plural': 'Термін віз',
            },
        ),
        migrations.CreateModel(
            name='VisaType',
            fields=[
                ('visa_code', models.IntegerField(primary_key=True, serialize=False)),
                ('nomination', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Типи віз',
                'verbose_name_plural': 'Типи віз',
            },
        ),
        migrations.CreateModel(
            name='Visa',
            fields=[
                ('number_visa', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('username', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('series_passport', models.CharField(max_length=255)),
                ('date_issue', models.DateField()),
                ('valid_date', models.DateField()),
                ('phone', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('payment_amount', models.IntegerField(null=True, verbose_name=VisaRegistration.models.VisaTariff)),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='VisaRegistration.country')),
                ('status', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='VisaRegistration.visastatus')),
                ('tariff_number', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='VisaRegistration.visatariff')),
                ('visa_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='VisaRegistration.visatype')),
            ],
            options={
                'verbose_name': 'Заявки на візи',
                'verbose_name_plural': 'Виза',
            },
        ),
    ]
