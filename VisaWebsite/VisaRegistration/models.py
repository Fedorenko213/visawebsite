from shortuuidfield import ShortUUIDField
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class User(AbstractUser):
    birthday = models.DateField(null=True, blank=True)


class VisaType(models.Model):
    visa_code = models.IntegerField(primary_key=True)
    nomination = models.CharField(max_length=255)

    def __str__(self):
        return str(self.nomination)

    class Meta:
        verbose_name = 'Типи віз'
        verbose_name_plural = "Типи віз"


class VisaCountry(models.Model):
    country_code = models.IntegerField(primary_key=True)
    country = models.CharField(max_length=255)

    def __str__(self):
        return str(self.country)

    class Meta:
        verbose_name = 'Країни віз'
        verbose_name_plural = "Країни віз"


class VisaTariff(models.Model):
    tariff_number = models.IntegerField(primary_key=True)
    validity_period = models.DecimalField(max_digits=10, decimal_places=0, null=True)
    coefficient = models.DecimalField(max_digits=10, decimal_places=4, null=True)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=4, null=True)

    def __str__(self):
        return str(self.validity_period)

    class Meta:
        verbose_name = 'Термін віз'
        verbose_name_plural = "Термін віз"


class VisaStatus(models.Model):
    status_code = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=255)

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = 'Статусы віз'
        verbose_name_plural = "Статусы віз"


class Visa(models.Model):
    code_visa = ShortUUIDField(primary_key=True, max_length=10, editable=False, help_text=u'User UUID')
    username = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    series_passport = models.CharField(max_length=255)
    country = models.ForeignKey(VisaCountry, null=True, on_delete=models.SET_NULL)
    visa_type = models.ForeignKey(VisaType, null=True, on_delete=models.SET_NULL)
    tariff_number = models.ForeignKey(VisaTariff, null=True, on_delete=models.SET_NULL)
    date_issue = models.DateField()
    valid_date = models.DateField(null=True, blank=True,
                                  help_text='Заповнюється автоматично по полю з вибраного тарифу')
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True,
                                         help_text='Заповнюється автоматично по полю з вибраного тарифу')
    status = models.ForeignKey(VisaStatus, default=1, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.code_visa)

    class Meta:
        verbose_name = 'Заявки на візи'
        verbose_name_plural = "Виза"