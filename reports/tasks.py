#!/devicehealth/csvparser.py
from os import listdir
from os.path import isfile, join


import csv
from devicehealth.settings import BASE_DIR
from reports.models import *
from datetime import datetime

from celery import task
from celery.contrib import rdb

report_path=BASE_DIR+'/static/reports'
suffix = '.csv'

@task()
def importcsv():
    report_files = [ \
        join(report_path, file) for file in listdir(report_path) \
        if file.endswith( suffix ) and isfile(join(report_path, file))
    ]
    for file in report_files: 
        reader = csv.DictReader(open(file))
        count = 0;
        header = [];
        # dviceReport = DeviceReport()
        for row in reader:
        	count += 1
        	obj, created = DeviceReport.objects.get_or_create(
    		    report_timestamp=datetime.strptime(row['timestamp'], '%Y-%m-%dT%H:%M:%SZ'),
    		    report_id=row['id'],
    		    report_type=row['type'],
    		    report_status=row['status']
    		)

