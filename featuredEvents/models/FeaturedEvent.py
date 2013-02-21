import datetime
import logging
import os, random, string

from django.db import models

logger = logging.getLogger(__name__)

class FeaturedEvent(models.Model):
    presenter = models.CharField("presenter", max_length=256)
    eventDateTime = models.DateTimeField("event datetime")
    dateCreated = models.DateTimeField("date created", auto_now_add=True)
    description = models.CharField("description", max_length=100)
    venueName = models.CharField("venue name", max_length=100)
    city = models.CharField("city", max_length = 64)
    url = models.CharField("url", max_length=256, blank=True, null=True)

    class Meta:
        app_label = "featuredEvents"

    def __str__(self):
        return "%s @ %s, %s" % (self.presenter, self.venueName, self.city)
