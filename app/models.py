from django.db import models

class Complaint(models.Model):
    name = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=50, default="Pending")
    class Meta:
        db_table = "complaint_tbl"

