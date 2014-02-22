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

    name = models.CharField(max_length=200, verbose_name=_("Name"))

    def __unicode__(self):
        return self.name


class Vendors(dd.Table):
    model = Vendor
    column_names = "name *"


class Manufacturer(dd.Model):
    class Meta:
        verbose_name = _("Manufacturer")
        verbose_name_plural = _("Manufacturers")

    name = models.CharField(max_length=200, verbose_name=_("Name"))

    def __unicode__(self):
        return self.name


class Manufacturers(dd.Table):
    model = Manufacturer
    column_names = "name *"


class Product(dd.Model):
    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    prodtype_list = (
        ("pc", "Computer"),
        ("care", "Service Care"),
        ("periph", "Peripherals"),
        ("storage", "Storage"),
        ("comp", "Components"),
        ("network", "Networking"),
        ("software", "Software"),
        ("communication", "Communication")
    )
    ## Product Types - Example Computers
    prodtype = models.CharField(max_length=200, choices=prodtype_list, default="pc", verbose_name=_("Product Type"))
    ## Manufacturer -> Foreign Key
    manufacturer = models.ForeignKey(Manufacturer)
    ## Name - Example: MacBook Air
    name = models.CharField(max_length=200, verbose_name=_("Name"))
    ## Model Number - Example: A1369
    model_number = models.CharField(max_length=200, verbose_name=_("Model Number"))
    ## line - Example: late 2010
    line = models.CharField(max_length=200, verbose_name=_("Product Line"))
    ## productionbegin
    production_begin = models.DateField(null=True, verbose_name=_("Production begin / Release"))
    ##
    supported = models.BooleanField(default=True, verbose_name=_("Still supported by manufacturer"))
    ## Image Uppload
    @dd.virtualfield(dd.HtmlBox())
    def product_image(self, ar):
        url = self.get_image_url()
        s = "<img src=\"%s\" height=\"100%%\" />" % url
        s = "<a href=\"%s\" target=\"_blank\">%s</a>" % (url, s)
        return s

    def get_image_url(self):
        try:
            im = ProductImage.objects.get(product=self, default_image=True)
        except ProductImage.DoesNotExist:
            return "foo.jpg"

        return im.file.url

    def __unicode__(self):
        return self.name


class ProductDetail(dd.FormLayout):
    main = """
    image_box:20 spec_box:80
    SpecsByProduct
    OptionsByProduct
    """

    image_box = "product_image"

    spec_box = """prodtype manufacturer name
    model_number line production_begin supported
    """

class Products(dd.Table):
    model = Product
    column_names = "manufacturer name line *"

    insert_layout = """
    prodtype manufacturer
    name
    model_number
    line
    production_begin
    supported
    """

    detail_layout = ProductDetail()

class ProductSpec(dd.Sequenced):
    class Meta:
        verbose_name = _("Product specification")
        verbose_name_plural = _("Product specifications")

    product = models.ForeignKey(Product)
    specification = models.CharField(max_length=200, verbose_name=_("Specification"))
    specification_value = models.CharField(max_length=200, verbose_name=_("Value"))

    def __unicode__(self):
        return self.name


class ProductSpecs(dd.Table):
    model = ProductSpec
    preview_limit = 0


class SpecsByProduct(ProductSpecs):
    master_key = 'product'
    column_names = ("specification:20 specification_value:80 move_buttons *")
    order_by = ["seqno"]


class ProductOption(dd.Sequenced):
    class Meta:
        verbose_name = _("Product option")
        verbose_name_plural = _("Product options")

    product = models.ForeignKey(Product)
    option = models.CharField(max_length=200, verbose_name=_("Option"))
    option_value = models.CharField(max_length=200, verbose_name=_("Value"))

    def __unicode__(self):
        return self.name


class ProductOptions(dd.Table):
    model = ProductOption
    preview_limit = 0


class OptionsByProduct(ProductOptions):
    master_key = 'product'
    column_names = ("option:20 option_value:80 move_buttons *")


class ProductImage(dd.Sequenced, dd.Uploadable):
    class Meta:
        verbose_name = _("Product Image")
        verbose_name_plural = _("Product Images")

    product = models.ForeignKey(Product)
    default_image = models.BooleanField(default=False)


class ProductImages(dd.Table):
    model = ProductImage

class ImagesByProduct(ProductImages):
    master_key = "product"


def setup_main_menu(site, ui, profile, m):
    m = m.add_menu("products", _("Products"))
    m.add_action(Vendors)
    m.add_action(Manufacturers)
    m.add_action(Products)


def setup_explorer_menu(site, ui, profile, m):
    m = m.add_menu("products", _("Products"))
    m.add_action(ProductSpecs)
    m.add_action(ProductOptions)
