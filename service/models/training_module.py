from django.db import models

class TrainingModule(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_by = models.ForeignKey('Trainer', on_delete=models.CASCADE, related_name='modules')
    resources = models.ManyToManyField('Resource', related_name='modules', db_table='module_resources',blank=True)

    class Meta:
        db_table = 'training_module'
        ordering = ['-id']
        
    def __str__(self):
        return f"{self.title} (By: {self.created_by.name})"