from django.contrib import admin
from suit.apps import DjangoSuitConfig


class SuitConfig(DjangoSuitConfig):
    layout = 'horizontal'
    admin.AdminSite.site_title = 'Testing'
    admin.AdminSite.site_header = 'Testing'
    admin.AdminSite.enable_nav_sidebar = False
