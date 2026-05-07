from django.db import models

class Trainer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    class Meta:
        db_table = 'trainer' 
        ordering = ['-id']

    def __str__(self):
        return self.name