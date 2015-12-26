from django.db import models
from django.utils.translation import ugettext_lazy as _


class Software(models.Model):
    software_choices = (
        ('OS', _('Operative System')),
        ('AP', _('Application')),
        ('SU', _('Support and Problem Fixing')),
        ('OT', _('Other'))
    )
    name = models.CharField(_('Name'), max_length=200)
    version = models.CharField(_('Version'), max_length=200)
    type = models.CharField(_('Type'), choices=software_choices, max_length=200)

    def __unicode__(self):
        return u"%s - %s v.%s" % (self.type, self.name, self.version)


class HardwareManufacturer(models.Model):
    name = models.CharField(_('Name'), max_length=200, blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('Hardware Manufacturer')
        verbose_name_plural = _('Hardware Manufacturers')


class Hardware(models.Model):
    hardware_choices = (
        ('MOB', _('Mobile')),
        ('NOTE', _('Notebook')),
        ('NET', _('Netbook')),
        ('TAB', _('Tablet')),
        ('DES', _('Desktop')),
        ('OTH', _('Other'))
    )
    type = models.CharField(_('Type'), choices=hardware_choices, max_length=200)
    manufacturer = models.ForeignKey(HardwareManufacturer, verbose_name=_('Manufacturer'), blank=True, null=True)
    model = models.CharField(_('Model'), max_length=200, blank=True, null=True)
    serial = models.CharField(_('Serial'), max_length=200, blank=True, null=True)

    def __unicode__(self):
        return u"%s, %s, %s" % (self.type, self.manufacturer, self.model)
