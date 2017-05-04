from __future__ import unicode_literals

from django.db import models
from django.conf import settings

"""	Database Model for Patient Sessions

	This creates Database mappings as given below
	These represents individual columns in a Relational Database

	:patient_id - ID assigned to patient when the app is installed
	:session_name - name of session, by default date as a string
	:remarks - miscellaneous remarks
	:xray - xray  Image
	:bloodwork - bloodwork Image
	:shared_file - A file that was shared over WIFI"""

#upload Path is calculated dynamically to sort sessions by patint folders
def upload_to(instance, filename):
    return '{}/{}/{}'.format(instance.patient_id,instance.session_name, filename)

	
class RawSession(models.Model):

    patient_id = models.IntegerField()
    session_name = models.CharField(max_length=100, db_index=True, blank=True)
    remarks = models.CharField(max_length=50, blank=True)
    xray = models.ImageField(blank=True, null=True, upload_to=upload_to)
    bloodwork = models.ImageField(blank=True, null=True, upload_to=upload_to)
    shared_file = models.FileField(blank=True, null=True, upload_to=upload_to)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
    	return 'Patient: %s, Session: %s'%(self.patient_id, self.session_name)

class RaspDataSet(models.Model):
    temp = models.FloatField()
    humidity = models.FloatField()
    data3 = models.FloatField()
    data4 = models.FloatField()
    data5 = models.FloatField()
    data6 = models.FloatField()
    data7 = models.FloatField()
    data8 = models.FloatField()

    indexed_at = models.DateTimeField(auto_now=True)
