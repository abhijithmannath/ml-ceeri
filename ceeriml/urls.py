"""ceeriml URL Configuration
This file lists all available URL Endpoints
"""
from django.conf.urls import url
from django.contrib import admin
from geo.views import log_location
from session.views import RawSessionView, PiDataView
from django.conf.urls.static import static
from django.conf import settings




urlpatterns = [
    url(r'^log-location/',log_location),
    url(r'^new-session/',RawSessionView.as_view()),
     url(r'^data-session/',PiDataView.as_view()),
     url(r'^', admin.site.urls),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
