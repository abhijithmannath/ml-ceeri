from rest_framework import serializers
from .models import RawSession


#This Serializes and Deserializes Request and Response data for 0 or more sessions

class RawSessionSerializer(serializers.ModelSerializer):

	class Meta:
		model = RawSession
		fields = ('patient_id','session_name','remarks','xray','bloodwork','shared_file')