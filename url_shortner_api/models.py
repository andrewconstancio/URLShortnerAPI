from django.db import models

class URL(models.Model):
    url = models.CharField(max_length=200)
    slug = models.CharField(max_length=15)
    date_created = models.DateTimeField()

def __str__(self):
        return f"Short Url for: {self.url} is {self.slug}"