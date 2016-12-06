from __future__ import unicode_literals

from django.db import models

class Contact (models.Model):
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    companyName = models.CharField(max_length=30)
    telephone = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" % self.title
