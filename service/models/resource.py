from django.db import models

class Resource(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='resources/')

    class Meta:
        db_table = 'resource'
        ordering = ['-id']

    def __str__(self):
        return self.name