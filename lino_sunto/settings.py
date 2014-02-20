# -*- coding: UTF-8 -*-
from lino.projects.std.settings import Site

class Site(Site):
        title = "Lino Sunto"
        def get_installed_apps(self):
            yield super(Site, self).get_installed_apps()
            yield 'lino_sunto.products'
            yield 'lino_sunto.support'

SITE = Site(globals())
SECRET_KEY = '4tnn118570xptxmd33_v=v)k&(3z(j5$r&pa1*ei1$pqj6hqc!'

DEBUG = True