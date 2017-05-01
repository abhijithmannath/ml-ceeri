from django.shortcuts import render
from .models import GeoLocation
from django.http import HttpResponse


def log_location(request):
	"""
	:params
		:lat  - latitude
		:lon  - longitude
		:user_agent  - useful for IOT applications that needs to log the client 
						that send the location
	"""
	if request.method == 'GET':
		user_agent = request.GET.get('user_agent','test')
		try:
			lat = request.GET['lat']
			lon = request.GET['lon']
			GeoLocation.objects.create(user_agent=user_agent,lat=lat,lon=lon)
		except:
			return HttpResponse(0, status=500)

	return HttpResponse(1, status=200)
