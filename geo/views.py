from django.shortcuts import render
from .models import GeoLocation
from django.http import HttpResponse

# Create your views here.
def log_location(request):
	if request.method == 'GET':
		user_agent = request.GET.get('user_agent','test')
		try:
			lat = request.GET['lat']
			lon = request.GET['lon']
			GeoLocation.objects.create(user_agent=user_agent,lat=lat,lon=lon)
		except:
			return HttpResponse(0, status=500)

	return HttpResponse(1, status=200)
