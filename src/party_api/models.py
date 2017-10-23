from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Party(models.Model):
    name = models.CharField(max_length=100, )
    description = models.CharField(max_length=255, blank=True, default='')

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name

