from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.test import TestCase

from registrasi.models import Supplier, Material


# Create your tests here.


class SupplierTestCase(TestCase):
    def setUp(self):
        supplier1 = Supplier.objects.create(name="PT. ABC")
        supplier2 = Supplier.objects.create(name="PT. CDE")
        self.supplier1 = supplier1.name
        self.supplier2 = supplier2.name

    def test_get_supplier(self):
        self.assertEqual(self.supplier1, "PT. ABC")
        self.assertEqual(self.supplier2, "PT. CDE")


class MaterialTestCase(TestCase):
    def setUp(self):
        supplier1 = Supplier.objects.create(name="PT. ABC")
        TYPES = Material.TYPES
        self.m1 = Material.objects.create(code="1Q2W", name="Biru Tua", type=TYPES[0], buy_price=88, supplier=supplier1)
        self.m2 = Material.objects.create(code="1Q3E", name="Biru Muda", type=TYPES[1], buy_price=87, supplier=supplier1)
        self.m3 = Material.objects.create(code="1Q5T", name="Tosca", type=TYPES[1], buy_price=68, supplier=supplier1)
        self.m4 = Material.objects.create(code="1Q4R", name="Coklat", type=TYPES[2], buy_price=99, supplier=supplier1)

    def test_get_material(self):
        self.assertEqual(self.m1.__str__(), '1Q2W - Biru Tua')

    def test_uniq_code(self):
        supplier1 = Supplier.objects.create(name="PT. ABC")
        TYPES = Material.TYPES
        a = Material(code="1Q4R", name="Coklat", type=TYPES[2], buy_price=85, supplier=supplier1)
        with self.assertRaises(Exception) as raised:
            a.save()
        self.assertEqual(IntegrityError, type(raised.exception))

    def test_buy_price_greater_than_100(self):
        supplier1 = Supplier.objects.create(name="PT. ABC")
        TYPES = Material.TYPES
        a = Material(code="1Q4RR", name="Coklat", type=TYPES[2], buy_price=100, supplier=supplier1)
        with self.assertRaises(Exception) as raised:
            a.save()
        self.assertEqual(ValidationError, type(raised.exception))

    def test_buy_price(self):
        supplier1 = Supplier.objects.create(name="PT. ABC")
        TYPES = Material.TYPES
        buy_price = 85
        a = Material(code="1Q4RR", name="Coklat", type=TYPES[2], buy_price=buy_price, supplier=supplier1)
        a.save()
        self.assertEqual(a.buy_price, buy_price)
