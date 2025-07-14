from django.db import models

# Create your models here.
class Sample(models.Model):
    hash = models.CharField(max_length=64, unique=True)
    filename = models.CharField(max_length=255)
    upload_date = models.DateTimeField(auto_now_add=True)
    analyzed = models.BooleanField(default=False)

    def __str__(self):
        return self.filename