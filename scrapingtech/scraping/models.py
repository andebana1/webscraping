from django.db import models

# Create your models here.

class TechModel(models.Model):
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

    class Admin:
        pass
