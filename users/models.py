from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    name = models.CharField(null=True, blank=True, max_length=255,)
    mail = models.EmailField(max_length=150, null=True, blank=True,)
    roles = models.ManyToManyField("users.Role", blank=True, related_name="user_roles",)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})


class Role(models.Model):
    "Generated Model"
    name = models.CharField(max_length=150,)
