from django.db import models

# Create your models here.
class CompletionInfo(models.Model):
    date_and_time = models.DateTimeField(help_text='When the site is expected to be completed')