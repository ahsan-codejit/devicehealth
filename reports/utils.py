from django.db.models import Sum, Count, Max
from datetime import datetime, timedelta
from time import gmtime, strftime

from reports.models import *

def format_date_list(dateString):
	return {
		'date': strftime('%d %b %Y',datetime.strptime(dateString,'%Y-%m-%d').timetuple()), 
		'value': dateString
	}

def format_day_count(day):
	return {
		'date': strftime('%d %b %Y',datetime.strptime(day['day'],'%Y-%m-%d').timetuple()), 
		'count': day['count']
	}

def format_device_types_count(device_type, selected_date):
	last_week_date = selected_date - timedelta(days=7)
	last_week_next_date = last_week_date + timedelta(days=1)
	lastweekoccurence = DeviceReport.objects \
		.filter(report_timestamp__gte=last_week_date, report_timestamp__lt=last_week_next_date, 
			report_type=device_type['report_type']).count()
	if not lastweekoccurence: 
		lastweekoccurence = 0
	return {
		'device_type': device_type['report_type'],
		'count': device_type['count'],
		'percentage': str(get_change_percentage(device_type['count'],lastweekoccurence))+'%'
	}

def get_change_percentage(current, previous):
    if current == previous:
        return 0.0
    try:
       return round((abs(current - previous)/previous)*100.0, 2)
    except ZeroDivisionError:
        return 100.0