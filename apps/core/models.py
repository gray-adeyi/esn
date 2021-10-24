from django.db import models

# Create your models here.


class Site(models.Model):
    """
    This model holds the sites information
    """
    name = models.CharField(max_length=200, )
    domain = models.URLField(blank=True)
    about = models.TextField()
    mission = models.TextField()
    vision = models.TextField()
    favicon = models.ImageField()
    appleicon = models.ImageField()
    logo = models.ImageField()
    address = models.TextField()

    def __str__(self):
        return self.name


class PhoneNumber(models.Model):
    site = models.ForeignKey(
        Site, related_name='numbers', on_delete=models.CASCADE)
    # Note: if it is ineffective to store numbers in the format 080-xxx
    number = models.IntegerField()
    # i'll have to change the field type to `models.CharField`

    def __str__(self) -> str:
        return self.site.name


class SocialAccount(models.Model):
    OPTIONS = (
        ('facebook', 'Facebook'),
        ('instagram', 'Instagram'),
        ('twitter', 'Twitter'),
    )
    site = models.ForeignKey(
        Site, related_name='social_accounts', on_delete=models.CASCADE)
    name = models.CharField(max_length=20, choices=OPTIONS)
    url = models.URLField()


class Event(models.Model):
    """
    This models stores info all events
    """
    OPTIONS = (
        ('meeting','Meeting'),
        ('workshop','Workshop'),
        ('seminar','Seminar'),
    )
    title = models.CharField(max_length=200)
    poster = models.ImageField()
    location = models.CharField(max_length=200)
    date_time = models.DateTimeField()
    duration = models.DurationField(blank=True)
    info = models.TextField(help_text="more helpful informations...")

    def __str__(self) -> str:
        return self.title