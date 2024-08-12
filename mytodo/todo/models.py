from django.db import models

from django.contrib.admin.widgets import AdminDateWidget

class Task(models.Model):
    title = models.CharField(max_length=35)
    description = models.TextField(null=True, blank=True)
    due_date = models.TextField()
    due_time = models.TimeField()
    completed = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return f'{self.title}'
    
    
