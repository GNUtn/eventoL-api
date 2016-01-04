from django.db import models
from event.models import Event
from django.contrib.auth.models import User
from device.models import Hardware, Software
from user.models import InstalationAttendee, Installer
from django.utils.translation import ugettext_lazy as _, ugettext_noop as _noop


class Activity(models.Model):
    event = models.ForeignKey(Event, verbose_name=_noop('Event'))
    title = models.CharField(_('Title'), max_length=50, blank=True, null=True)
    long_description = models.TextField(_('Long Description'))
    confirmed = models.BooleanField(_('Confirmed'), default=False)
    abstract = models.TextField(_('Abstract'), help_text=_('Short idea of the talk (Two or three sentences)'))

    def __unicode__(self):
        return u"%s: %s" % (self.event, self.title)

    class Meta:
        ordering = ['title']
        verbose_name = _('Activity')
        verbose_name_plural = _('Activities')


class TalkType(models.Model):
    """
    Type of talk. For example: Talk, Workshop, Debate, etc.
    """
    name = models.CharField(_('Name'), max_length=200)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('Talk Type')
        verbose_name_plural = _('Talk Types')


class TalkProposal(models.Model):
    level_choices = (
        ('1', _('Beginner')),
        ('2', _('Medium')),
        ('3', _('Advanced')),
    )
    activity = models.ForeignKey(Activity, verbose_name=_noop('Activity'))
    type = models.ForeignKey(TalkType, verbose_name=_('Type'))
    speakers_names = models.CharField(_('Speakers Names'), max_length=600,
                                      help_text=_("Comma separated speaker's names"))
    speakers_email = models.CharField(_('Speakers Emails'), max_length=600,
                                      help_text=_("Comma separated speaker's emails"))
    labels = models.CharField(_('Labels'), max_length=200,
                              help_text=_('Comma separated tags. i.e. Linux, Free Software, Debian'))
    presentation = models.FileField(_('Presentation'), upload_to='talks', blank=True, null=True, help_text=_(
        'Any material you are going to use for the talk (optional, but recommended)'))
    level = models.CharField(_('Level'), choices=level_choices, max_length=100,
                             help_text=_("The talk's Technical level"), default='Beginner')

    def __unicode__(self):
        return u"%s: %s" % (self.activity.event, self.activity.title)

    class Meta:
        verbose_name = _('Talk Proposal')
        verbose_name_plural = _('Talk Proposals')


class Room(models.Model):
    event = models.ForeignKey(Event, verbose_name=_noop('Event'))
    name = models.CharField(_('Name'), max_length=200, help_text=_('i.e. Classroom 256'))
    for_type = models.ForeignKey(TalkType, verbose_name=_('For talk type'),
                                 help_text=_('The type of talk the room is going to be used for.'))

    def __unicode__(self):
        return u"%s - %s" % (self.event.name, self.name)

    class Meta:
        verbose_name = _('Room')
        verbose_name_plural = _('Rooms')
        ordering = ['name']


class Talk(models.Model):
    talk_proposal = models.OneToOneField(TalkProposal, verbose_name=_('TalkProposal'), blank=True, null=True)
    room = models.ForeignKey(Room, verbose_name=_('Room'))
    start_date = models.DateTimeField(_('Start Time'))
    end_date = models.DateTimeField(_('End Time'))

    def __unicode__(self):
        return u"%s - %s (%s - %s)" % (self.talk_proposal.activity.event.name, self.talk_proposal.activity.title,
                                       self.start_date.strftime("%H:%M"), self.end_date.strftime("%H:%M"))

    def __cmp__(self, other):
        return -1 if self.start_date.time() < other.start_date.time() else 1

    def schedule(self):
        return u"%s - %s" % (self.start_date.strftime("%H:%M"), self.end_date.strftime("%H:%M"))

    def get_schedule_info(self):
        talk = {
            'room': self.room.name,
            'start_date': self.start_date.strftime('%m/%d/%Y %H:%M'),
            'end_date': self.end_date.strftime('%m/%d/%Y %H:%M'),
            'title': self.talk_proposal.activity.title,
            'speakers': self.talk_proposal.speakers_names,
            'type': self.talk_proposal.type.name
        }
        return talk

    class Meta:
        verbose_name = _('Talk')
        verbose_name_plural = _('Talks')


class Comment(models.Model):
    created = models.DateTimeField()
    body = models.TextField()
    activity = models.ForeignKey(Activity, verbose_name=_noop('Activity'))
    user = models.ForeignKey(User, verbose_name=_('User'))

    def __unicode__(self):
        return u"%s: %s" % (self.user, self.activity)

    def save(self, *args, **kwargs):
        """Email when a comment is added."""
        # TODO: Email when a comment is added.
        if "notify" in kwargs:
            del kwargs["notify"]
        super(Comment, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')


class Installation(models.Model):
    hardware = models.ForeignKey(Hardware, verbose_name=_('Hardware'), blank=True, null=True)
    software = models.ForeignKey(Software, verbose_name=_('Software'), blank=True, null=True)
    attendee = models.ForeignKey(InstalationAttendee, verbose_name=_('Attendee'),
                                 help_text=_('The owner of the installed hardware'))
    installer = models.ForeignKey(Installer, verbose_name=_('Installer'), related_name='installed_by', blank=True,
                                  null=True)
    notes = models.TextField(_('Notes'), blank=True, null=True,
                             help_text=_('Any information or trouble you found and consider relevant to document'))

    def __unicode__(self):
        return u"%s, %s, %s" % (self.attendee, self.hardware, self.software)

    class Meta:
        verbose_name = _('Installation')
        verbose_name_plural = _('Installations')
