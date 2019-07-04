from django.db import models

class Book(models.Model):
    title = models.TextField(max_length=32, blank=False, null=False)
