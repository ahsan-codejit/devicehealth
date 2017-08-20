from django.shortcuts import render_to_response, render
from django.template import RequestContext

from django.db.models import Sum, Count, Max
from datetime import datetime, timedelta
from time import gmtime, strftime

from reports.utils import *
from reports.models import *

# HomePage.
def index(request):
	context = {}
	return render(request, 'index.html', context)

def devices_report(request):
	context = {}
	try:
		devices_types  = DeviceReport.objects.values('report_type').distinct()
		context['devices_types'] = [dt['report_type'] for dt in devices_types]
		# import pdb; pdb.set_trace()
		device_type = request.POST.get('device_type')
		if device_type:
			context['selected_type'] = device_type
			# list of last 30 days
			last_date = DeviceReport.objects.aggregate(Max('report_timestamp'))['report_timestamp__max']
			start_date = last_date - timedelta(days=30)
			days = DeviceReport.objects \
			    .filter(report_timestamp__gt=start_date, report_type=device_type) \
			    .extra({'day': 'date(report_timestamp)'}) \
			    .values('day') \
			    .annotate(count=Count('report_id'))

			context['reports_by_dates'] = [format_day_count(day) for day in days]
	except Exception:
		pass
	return render(request, 'devices.html', context)

def days_report(request):
	# import pdb; pdb.set_trace()
	context = {}
	try:
		timestamps = DeviceReport.objects.extra({'date':'date(report_timestamp)'}).values('date').distinct() 
		context['dates'] = [format_date_list(ts['date']) for ts in timestamps]

		selected_day = request.POST.get('day')
		if selected_day:
			context['selected_day'] = selected_day
			selected_date = datetime.strptime(selected_day, '%Y-%m-%d')
			next_date = selected_date + timedelta(days=1)
			device_types = DeviceReport.objects \
				.filter(report_timestamp__gte=selected_date, report_timestamp__lt=next_date) \
				.values('report_type') \
				.distinct() \
				.annotate(count=Count('report_id')) \
				.order_by('-count')[:10]
			context['device_types'] = [format_device_types_count(dtype, selected_date) for dtype in device_types]
	except Exception:
		pass

	return render(request, 'days.html', context)
