# reports/models.py
from django.db import models

class DeviceReport(models.Model):
    report_id = models.CharField(max_length=128)
    report_type = models.CharField(max_length=128)
    report_status = models.CharField(max_length=50)
    report_timestamp = models.DateTimeField()

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'device_reports'

    def __unicode__(self):
        return str(self.id)