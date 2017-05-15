# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Sms(models.Model):
	to = models.CharField(max_length=1000)
	message = models.TextField()


