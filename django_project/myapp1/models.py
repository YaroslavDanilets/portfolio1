from django.db import models

# Create your models here.

class Worker(models.Model):
    first_name = models.CharField(max_length=20, blank=False)
    second_name = models.CharField(max_length=20, blank=False)
    salary = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.second_name}: {self.salary}'
