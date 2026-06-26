from django.db import models
from datetime import datetime as dt

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000000)
    created_at = models.DateTimeField(default=dt.now, blank=True)

    def __str__(self):
        return self.title
