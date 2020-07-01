from django.db import models

# Create your models here.
class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    title = models.CharField(max_length=100, default='N/A')
    github = models.URLField(max_length=200, default='https://github.com/alexliou')

    def __str__(self):
        return self.summary
