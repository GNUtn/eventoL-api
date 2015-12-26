from django.db import models
from event.models import Event
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _, ugettext_noop as _noop


class EventoLUser(models.Model):
    user = models.OneToOneField(User, verbose_name=_('User'), blank=True, null=True)
    event = models.ForeignKey(Event, verbose_name=_noop('Event'), help_text=_('Event you are going to collaborate'))
    assisted = models.BooleanField(_('Assisted'), default=False)

    def __unicode__(self):
        return str(self.user)

    class Meta:
        verbose_name = _('EventoL User')
        verbose_name_plural = _('EventoL User')


class Collaborator(models.Model):
    eventolUser = models.ForeignKey(EventoLUser, verbose_name=_('EventoL User'))
    assignation = models.CharField(_('Assignation'), max_length=200, blank=True, null=True,
                                   help_text=_('Assignations given to the user (i.e. Talks, Coffee...)'))
    time_availability = models.CharField(_('Time Availability'), max_length=200, blank=True, null=True, help_text=_(
        'Time gap in which you can help during the event. i.e. "All the event", "Morning", "Afternoon"...'))
    phone = models.CharField(_('Phone'), max_length=200, blank=True, null=True)
    address = models.CharField(_('Address'), max_length=200, blank=True, null=True)
    additional_info = models.CharField(_('Additional Info'), max_length=200, blank=True, null=True,
                                       help_text=_('Any additional info you consider relevant'))

    class Meta:
        verbose_name = _('Collaborator')
        verbose_name_plural = _('Collaborators')


class Attendee(models.Model):
    eventolUser = models.ForeignKey(EventoLUser, verbose_name=_('EventoL User'))
    additional_info = models.CharField(_('Additional Info'), max_length=200, blank=True, null=True,
                                       help_text=_('Any additional info you consider relevant'))

    class Meta:
        verbose_name = _('Attendee')
        verbose_name_plural = _('Attendees')


class InstalationAttendee(models.Model):
    eventolUser = models.ForeignKey(EventoLUser, verbose_name=_('EventoL User'))
    installarion_additional_info = models.TextField(_('Additional Info'), blank=True, null=True,
                                                    help_text=_('i.e. Wath kind of PC are you bringing'))

    class Meta:
        verbose_name = _('Instalation Attendee')
        verbose_name_plural = _('Instalation Attendees')


class Installer(models.Model):
    installer_choices = (
        ('1', _('Beginner')),
        ('2', _('Medium')),
        ('3', _('Advanced')),
        ('4', _('Super Hacker'))
    )
    eventolUser = models.ForeignKey(EventoLUser, verbose_name=_('EventoL User'))
    level = models.CharField(_('Level'), choices=installer_choices, max_length=200,
                             help_text=_('Linux Knowledge level for an installation'))

    class Meta:
        verbose_name = _('Installer')
        verbose_name_plural = _('Installers')


class Speaker(models.Model):
    eventolUser = models.ForeignKey(EventoLUser, verbose_name=_('EventoL User'))

    class Meta:
        verbose_name = _('Speaker')
        verbose_name_plural = _('Speakers')

userTypes = {
    'Collaborators': Collaborator,
    'Attendees': Attendee,
    'Instalation Attendees': InstalationAttendee,
    'Speakers': Speaker,
    'Intallers': Installer
}


def getUserChoice():
    user_choice = []
    for key in userTypes.keys():
        user_choice.append((key, key))
    return user_choice
