"""
Model File for Products

"""

from django.utils.translation import ugettext_lazy as _
from django.db import models
from lino import dd


class Vendor(dd.Model):
    class Meta:
        verbose_name = _("Vendor")
        verbose_name_plural = _("Vendors")

    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Vendors(dd.Table):
    model = Vendor
    column_names = "name *"

class Manufacturer(dd.Model):
    class Meta:
        verbose_name = _("Manufacturer")
        verbose_name_plural = _("Manufacturers")

    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Manufacturers(dd.Table):
    model = Manufacturer
    column_names = "name *"

class Product(dd.Model):
    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    ## Manufacturer -> Foreign Key
    manufacturer = models.ForeignKey(Manufacturer)
    ## Name - Example: MacBook Air
    name = models.CharField(max_length=200)
    ## Model Number - Example: A1369
    model_number = models.CharField(max_length=200)
    ## line - Example: late 2010
    line = models.CharField(max_length=200)
    ## productionbegin
    production_begin = models.DateField(null=True)
    ##
    supported = models.BooleanField(default=True)


    def __unicode__(self):
        return self.name


class Products(dd.Table):
    model = Product
    column_names = "manufacturer name *"

    insert_layout = """
    manufacturer
    name
    model_number
    line
    production_begin
    supported
    """

    detail_layout = """
    manufacturer name
    model_number line production_begin supported
    SpecsByProduct
    OptionsByProduct
    """

class ProductSpec(dd.Model):
    class Meta:
        verbose_name = _("Product specification")
        verbose_name_plural = _("Product specifications")

    product = models.ForeignKey(Product)
    specification = models.CharField(max_length=200)
    specification_value = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class ProductSpecs(dd.Table):
    model = ProductSpec

class ProductOption(dd.Model):
    class Meta:
        verbose_name = _("Product option")
        verbose_name_plural = _("Product options")

    product = models.ForeignKey(Product)
    option = models.CharField(max_length=200)
    option_value = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class ProductOptions(dd.Table):
    model = ProductOption

class OptionsByProduct(ProductOptions):
    column_names = ("option option_value *")

class SpecsByProduct(ProductSpecs):
    column_names = ("specification specification_value *")

def setup_main_menu(site, ui, profile, m):
    m = m.add_menu("products", _("Products"))
    m.add_action(Vendors)
    m.add_action(Manufacturers)
    m.add_action(Products)

def setup_explorer_menu(site, ui, profile, m):
    m = m.add_menu("products", _("Products"))
    m.add_action(ProductSpecs)
    m.add_action(ProductOptions)
