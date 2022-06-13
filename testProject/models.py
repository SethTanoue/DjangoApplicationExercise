from django.db import models

class Memo(models.Model):
    message = models.CharField(max_length=200)