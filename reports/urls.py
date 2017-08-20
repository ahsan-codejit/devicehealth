# reports/urls.py

from django.conf.urls import url

from reports import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
    url(r'^reports/devices$', views.devices_report, name='devices_report'),
    url(r'^reports/days$', views.days_report, name='days_report'),
]