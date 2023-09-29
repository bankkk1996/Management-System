    
import os

from django.conf import settings
from django.contrib.sessions.models import Session
from django.db.models import CharField, PositiveSmallIntegerField, TextField, Model, ForeignKey, CASCADE, \
    FileField, DateTimeField, OneToOneField
from django.contrib.auth.models import AbstractUser, Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _


# According to django's official doc.
# "it’s highly recommended to set up a custom user model, even if the default User model is sufficient for you".



class User(AbstractUser):
    ADMIN = 0
    MAID= 1
    TECHNICIAN = 2
    GUEST = 3
    USER_TYPE = (
        (ADMIN, _('Admin')),
        (MAID, _('MAID')),
        (TECHNICIAN, _('Technician')),
        (GUEST, _('Guest')),
    )

    # A list of the field names that will be prompted for when creating a user
    # via the createsuperuser management command.
    REQUIRED_FIELDS = ['user_type']

    user_type = PositiveSmallIntegerField(choices=USER_TYPE, default=ADMIN)



@receiver(post_save, sender=User)
def add_to_default_group(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        group_name = 'Unknown'
        if user.user_type == User.ADMIN:
            group_name = 'Admin'
        elif user.user_type == User.MAID:
            group_name = 'Maid'
        elif user.user_type == User.TECHNICIAN:
            group_name = 'Technician'
        elif user.user_type == User.GUEST:
            group_name = 'Guest'
        group,_new = Group.objects.get_or_create(name=group_name)

        user.groups.add(group)


class UserSession(Model):
    user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    session = OneToOneField(Session, on_delete=CASCADE)


