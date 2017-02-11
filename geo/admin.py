from django.contrib import admin
from .models import GeoLocation

# Register your models here.
class GeoLocationAdmin(admin.ModelAdmin):
	list_display=['__str__','created']
	search_fields=['user_agent']

admin.site.register(GeoLocation, GeoLocationAdmin)