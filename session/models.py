from __future__ import unicode_literals

from django.db import models

# Create your models here
from django.conf import settings


def upload_to(instance, filename):
    return '{}/{}/{}'.format(instance.patient_id,instance.session_name, filename)


class RawSession(models.Model):
    patient_id = models.IntegerField()
    session_name = models.CharField(max_length=25, db_index=True, blank=True)
    remarks = models.CharField(max_length=50, blank=True)
    xray = models.ImageField(blank=True, null=True, upload_to=upload_to)
    bloodwork = models.ImageField(blank=True, null=True, upload_to=upload_to)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
    	return 'Patient: %s, Session: %s'%(self.patient_id, self.session_name)
