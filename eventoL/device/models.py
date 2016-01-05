from django.db import models
from django.utils.translation import ugettext_lazy as _

class SoftwareChoices(models.Model):
    """
        Options for Software Installations
    """
    description = models.CharField(_('Description'), max_length=200)

    def __unicode__(self):
        return self.description

    class Meta:
        verbose_name = _('Software Choice')
        verbose_name_plural = _('Software Choices')

class HardwareChoices(models.Model):
    """
        Options for Hardware Installations
    """
    description = models.CharField(_('Description'), max_length=200)

    def __unicode__(self):
        return self.description

    class Meta:
        verbose_name = _('Hardware Choice')
        verbose_name_plural = _('Hardware Choices')

class Software(models.Model):
    name = models.CharField(_('Name'), max_length=200)
    version = models.CharField(_('Version'), max_length=200)
    type = models.ForeignKey(SoftwareChoices, verbose_name=_('Type'))

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
    type = models.ForeignKey(HardwareChoices, verbose_name=_('Type'))
    manufacturer = models.ForeignKey(HardwareManufacturer, verbose_name=_('Manufacturer'), blank=True, null=True)
    model = models.CharField(_('Model'), max_length=200, blank=True, null=True)
    serial = models.CharField(_('Serial'), max_length=200, blank=True, null=True)

    def __unicode__(self):
        return u"%s, %s, %s" % (self.type, self.manufacturer, self.model)
