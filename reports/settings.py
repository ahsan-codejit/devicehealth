from celery.schedules import crontab

CELERY_BROKER_URL = 'amqp://guest@localhost//'
CELERY_RESULT_BACKEND = 'amqp://guest@localhost//'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_BEAT_SCHEDULE = {
	'importcsv': {
        'task': 'reports.tasks.importcsv',
        'schedule': crontab(minute = '*/5')
    }
}