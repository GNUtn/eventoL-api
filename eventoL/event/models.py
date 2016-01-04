import re
import datetime
from django.db import models
from ckeditor.fields import RichTextField
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import ugettext_lazy as _, ugettext_noop as _noop


def validate_url(url):
    if not re.match("^[a-zA-Z0-9-_]+$", url):
        raise ValidationError(_('URL can only contain letters or numbers'))


class Adress(models.Model):
    name = models.CharField(_('Name'), max_length=200)
    adress = models.CharField(_('Adress'), max_length=200)
    latitude = models.FloatField(_('Latitude'), validators=[MinValueValidator(-90), MaxValueValidator(90)])
    longitude = models.FloatField(_('Longitude'), validators=[MinValueValidator(-180), MaxValueValidator(180)])

    def __unicode__(self):
        return u"%s (%s-%s)" % (self.name, self.latitude, self.longitude)

    class Meta:
        ordering = ['name']


class Event(models.Model):
    name = models.CharField(_('Name'), max_length=200)
    date = models.DateField(_('Date'), help_text=_('Date of the event'))
    limit_proposal_date = models.DateField(_('Limit Proposal Date'), help_text=_('Date Limit of Talk Proposal'))
    url = models.CharField(_('URL'), max_length=200, help_text=_('URL for the sede i.e. CABA'),
                           validators=[validate_url])
    external_url = models.URLField(_('External URL'), blank=True, null=True, default=None, help_text=_(
        'If you want to use other page for your sede rather than eventoL\'s one, you can put the absolute url here'))
    email = models.EmailField(verbose_name=_('Email'))
    event_information = RichTextField(verbose_name=_('Event Information'), help_text=_('Event Information HTML'),
                                      blank=True, null=True)
    schedule_confirm = models.BooleanField(_('Schedule Confirm'), default=False)
    adress = models.ForeignKey(Adress, verbose_name=_('Adress'))

    def get_absolute_url(self):
        if self.external_url:
            return self.external_url
        return self.url

    @property
    def talk_proposal_is_open(self):
        return self.limit_proposal_date >= datetime.date.today()

    @property
    def registration_is_open(self):
        return self.date >= datetime.date.today()

    def __unicode__(self):
        return u"%s (%s)" % (self.name, self.adress.name)

    def get_geo_info(self):
        return {
            "lat": self.adress.latitude,
            "lon": self.adress.longitude,
            "name": self.adress.name
        }

    class Meta:
        ordering = ['name']


class ContactMessage(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    email = models.EmailField(verbose_name=_('Email'))
    message = models.TextField(verbose_name=_('Message'))

    class Meta:
        verbose_name = _('Contact Message')
        verbose_name_plural = _('Contact Messages')


class ContactType(models.Model):
    """
    For example:
        Name: Facebook
        Icon Class: fa-facebook-square
    """
    name = models.CharField(_('Name'), unique=True, max_length=200)
    icon_class = models.CharField(_('Icon Class'), max_length=200)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('Contact Type')
        verbose_name_plural = _('Contact Types')


class Contact(models.Model):
    type = models.ForeignKey(ContactType, verbose_name=_('Contact Type'))
    url = models.URLField(_noop('URL'))
    text = models.CharField(_('Text'), max_length=200)
    event = models.ForeignKey(Event, verbose_name=_noop('Event'), related_name='contacts')

    def __unicode__(self):
        return u"%s - %s" % (self.type.name, self.text)

    class Meta:
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')


class Image(models.Model):
    type = models.CharField(_('Type'), max_length=200)
    url = models.URLField(_noop('URL'))
    cropping = models.CharField(_('Text'), max_length=200)
    event = models.ForeignKey(Event, verbose_name=_noop('Event'))

    def __unicode__(self):
        return self.event.name

    class Meta:
        verbose_name = _('Image')
        verbose_name_plural = _('Images')
