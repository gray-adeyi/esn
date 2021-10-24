from django.db import models

# Create your models here.
class CompletionInfo(models.Model):
    """
    Holds details of the completion date of the site
    """
    date_and_time = models.DateTimeField(help_text='When the site is expected to be completed')