from django.db import models
from shortuuidfield import ShortUUIDField


class ProductionType(models.Model):
    name = models.TextField(null=False, blank=False)
    url = models.URLField(null=True, blank=True)


class ProductCategory(models.Model):
    name = models.CharField(max_length=512, null=False, blank=False)
    parent = models.ForeignKey("ProductCategory", on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.name


class Membership(models.Model):
    name = models.TextField(null=False, blank=False)
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


class Certificate(models.Model):
    name = models.TextField(null=False, blank=False)
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


class StoreCategory(models.Model):
    name = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.name


class StoreType(models.Model):
    name = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.name


class Payment(models.Model):
    name = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.name


class Store(models.Model):
    name = models.CharField(max_length=1024, null=False, blank=False)
    contact_name = models.CharField(max_length=1024, null=True, blank=True)
    contact_street = models.CharField(max_length=1024, null=True, blank=True)
    contact_zip = models.IntegerField(null=True, blank=True)
    contact_location = models.CharField(max_length=1024, null=True, blank=True)
    contact_phone = models.CharField(max_length=1024, null=True, blank=True)
    contact_mobile = models.CharField(max_length=1024, null=True, blank=True)
    contact_email = models.EmailField(null=True, blank=True)
    url = models.URLField(null=False, blank=False)
    production_type = models.ManyToManyField(ProductionType)
    product_categories = models.ManyToManyField(ProductCategory)
    certificates = models.ManyToManyField(Certificate)
    store_category = models.ForeignKey(StoreCategory, on_delete=models.DO_NOTHING, null=True, blank=True)
    store_type = models.ForeignKey(StoreType, on_delete=models.DO_NOTHING, null=True, blank=True)
    payments = models.ManyToManyField(Payment)
    languages = models.ManyToManyField(Language)
    uuid = ShortUUIDField(null=False, blank=True)

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        pass
