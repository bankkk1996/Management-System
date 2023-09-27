from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models import PositiveSmallIntegerField
from django.contrib.auth.models import User

ADMIN = 0
MAID_SUPERVISOR = 1
MAID= 2
TECHNICIAN = 3
GUEST = 4
USER_TYPE = (
    (ADMIN, _('Admin')),
    (MAID_SUPERVISOR, _('Maid Supervisor')),
    (MAID, _('MAID')),
    (TECHNICIAN, _('Technician')),
    (GUEST, _('Guest')),
)

# Create your models here.
# class User(models.Model):
#     ADMIN = 0
#     MAID_SUPERVISOR = 1
#     MAID= 2
#     TECHNICIAN = 3
#     GUEST = 4
#     USER_TYPE = (
#         (ADMIN, _('Admin')),
#         (MAID_SUPERVISOR, _('Maid Supervisor')),
#         (MAID, _('MAID')),
#         (TECHNICIAN, _('Technician')),
#         (GUEST, _('Guest')),
#     )

#     REQUIRED_FIELDS = ['user_type']
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     role = PositiveSmallIntegerField(choices=USER_TYPE)

class Maid(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')])
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    date_of_birth = models.DateField()
    id_card_number = models.CharField(max_length=20, unique=True)
    image = models.ImageField(upload_to='image/maid_images/')
    job_position = models.CharField(max_length=50)
    hire_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    employment_status = models.CharField(max_length=20, choices=[('working', 'Working'), ('resigned', 'Resigned')])
    
    def __str__(self):
        return self.user.get_full_name()
