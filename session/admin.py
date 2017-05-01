from django.contrib import admin
from .models import RawSession

# Register your models here.
class RawSessionAdmin(admin.ModelAdmin):
	list_display = ['patient_id','session_name','remarks']
	search_fields=['patient_id']

admin.site.register(RawSession, RawSessionAdmin)

#This Interface Registers the Admin Interface for Administration  purposes
#This is a secure endpoint only accessible to STAFF users
