"""
Model File for support

"""

from django.utils.translation import ugettext_lazy as _
from django.db import models
from lino import dd


class Customer(dd.Model):
    class Meta:
        verbose_name = _("Customer")
        verbose_name_plural = _("Customers")

    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Customers(dd.Table):
    model = Customer
    column_names = "name *"


class Support_Item(dd.Model):
    class Meta:
        verbose_name = _("Customer")
        verbose_name_plural = _("Customers")

    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Support_Items(dd.Table):
    model = Support_Item
    column_names = "name *"

def setup_main_menu(site, ui, profile, m):
    m = m.add_menu("customer", _("Customers"))
    m.add_action(Customers)