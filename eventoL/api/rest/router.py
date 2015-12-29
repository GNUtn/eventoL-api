from rest_framework import routers
from viewsets import UserViewSet
from activity import models as activity_model
from user import models as user_model
from event import models as event_model
from device import models as device_model
from builder import ViewSetBuilder

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

# Activity Model
router.register(r'talktype', ViewSetBuilder(activity_model.TalkType).build())
router.register(r'talkproposal', ViewSetBuilder(activity_model.TalkProposal).build())
router.register(r'room', ViewSetBuilder(activity_model.Room).build())
router.register(r'activity', ViewSetBuilder(activity_model.Activity).build())
router.register(r'comment', ViewSetBuilder(activity_model.Comment).build())
router.register(r'installation', ViewSetBuilder(activity_model.Installation).build())
router.register(r'talk', ViewSetBuilder(activity_model.Talk).build())

# User Models
router.register(r'installer', ViewSetBuilder(user_model.Installer).build())
router.register(r'instalationattendee', ViewSetBuilder(user_model.InstalationAttendee).build())
router.register(r'attendee', ViewSetBuilder(user_model.Attendee).build())
router.register(r'collaborator', ViewSetBuilder(user_model.Collaborator).build())
router.register(r'eventoluser', ViewSetBuilder(user_model.EventoLUser).build())
router.register(r'speaker', ViewSetBuilder(user_model.Speaker).build())

# Event Model
router.register(r'adress', ViewSetBuilder(event_model.Adress).build())
router.register(r'contact', ViewSetBuilder(event_model.Contact).build())
router.register(r'contactmessage', ViewSetBuilder(event_model.ContactMessage).build())
router.register(r'contacttype', ViewSetBuilder(event_model.ContactType).build())
router.register(r'event', ViewSetBuilder(event_model.Event).build())
router.register(r'image', ViewSetBuilder(event_model.Image).build())

# Device Model
router.register(r'hardware', ViewSetBuilder(device_model.Hardware).build())
router.register(r'hardwaremanufacturer', ViewSetBuilder(device_model.HardwareManufacturer).build())
router.register(r'software', ViewSetBuilder(device_model.Software).build())
