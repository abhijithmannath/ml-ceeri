from rest_framework import serializers
from .models import RawSession


class RawSessionSerializer(serializers.ModelSerializer):

	class Meta:
		model = RawSession
        fields = ('patient_id','session_name','remarks','xray','bloodwork')