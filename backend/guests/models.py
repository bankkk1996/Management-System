from django.db import models
from django.db.models import Model, CASCADE, DateField, IntegerField, CharField
from users.models import User
import datetime
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Guest(Model):
    MALE = "male"
    FEMALE = "female"
    UNKNOWN = "unknown"
    GENDER_CHOICES = (
        (MALE, _("Male")),
        (FEMALE, _("Female")),
        (UNKNOWN, _("Unknown"))
    )
    user = models.OneToOneField(User, on_delete=CASCADE, limit_choices_to={
                                'user_type': User.GUEST})
    birthdate = DateField(
        _("birthdate"), default=datetime.date.today, null=True, blank=True)
    age = IntegerField(_("age"), null=True, blank=True, default=0)
    gender = CharField(_("gender"), choices=GENDER_CHOICES,
                       default=UNKNOWN, max_length=10)