from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.
class Supplier(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class Material(models.Model):
    TYPES = (
        ('Fabric', 'Fabric'),
        ('Jeans', 'Jeans'),
        ('Cotton', 'Cotton')
    )
    code = models.CharField(max_length=8, unique=True)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=10, choices=TYPES)
    buy_price = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(99)])
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.code} - {self.name}'

    def save(self, *args, **kwargs):
        if self.buy_price <= 1 or self.buy_price >= 100 :
            raise ValidationError(f'{self.buy_price} minimum 1 maximal 99')
        super().save(*args, **kwargs)
