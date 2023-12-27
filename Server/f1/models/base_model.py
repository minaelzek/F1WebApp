from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField("Created On", auto_now_add=True)
    updated_on = models.DateTimeField("Updated On", auto_now=True)
    
    class Meta:
        abstract = True