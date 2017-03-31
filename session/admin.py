from django.contrib import admin
from .models import RawSession

# Register your models here.
class RawSessionAdmin(admin.ModelAdmin):
	list_display=['patient_id','created']
	search_fields=['patient_id']

admin.site.register(RawSession)

# Register your models here.
