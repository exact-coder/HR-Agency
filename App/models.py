from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Registered_email(models.Model):
    email = models.CharField(_("Email"), max_length=50)

    def __str__(self) -> str:
        return self.email