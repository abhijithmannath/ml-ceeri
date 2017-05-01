from django.db import models


"""
	 GeoLocation Database mappings
"""
class GeoLocation(models.Model):

    user_agent = models.CharField(max_length=30, db_index=True, blank=True)
    lat = models.DecimalField(max_digits=9,decimal_places=6)
    lon = models.DecimalField(max_digits=9,decimal_places=6)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
    	return 'user: %s, lat: %s, lon: %s'%(self.user_agent, self.lat, self.lon) 
