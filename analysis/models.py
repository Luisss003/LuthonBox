from django.db import models
from samples.models import Sample

# Create your models here.

class AnalysisJob(models.Model):
    sample = models.ForeignKey(Sample, on_delete=models.CASCADE)
    started_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(null=True, blank=True)
    success = models.BooleanField(default=False)
    log = models.TextField(blank=True)

    def __str__(self):
        return f"Job for {self.sample.filename} started at {self.started_at}"
