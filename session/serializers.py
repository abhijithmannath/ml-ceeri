from rest_framework import serializers
from .models import RawSession
from drf_base64.fields import Base64ImageField


class RawSessionSerializer(serializers.ModelSerializer):
	xray = Base64ImageField()
	bloodwork = Base64ImageField()

	class Meta:
		model = RawSession
		fields = ('patient_id','session_name','remarks','xray','bloodwork')