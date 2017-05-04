from rest_framework import serializers
from .models import RawSession, RaspDataSet


#This Serializes and Deserializes Request and Response data for 0 or more sessions

class RawSessionSerializer(serializers.ModelSerializer):

	class Meta:
		model = RawSession
		fields = ('patient_id','session_name','remarks','xray','bloodwork','shared_file')


class RaspDataSerializer(serializers.ModelSerializer):

	class Meta:
		model = RaspDataSet
		fields = ('temp','humidity','data3','data4','data5','data6','data7','data8')