from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.FAQ)
admin.site.register(models.Site)
admin.site.register(models.SiteSocialAccount)
admin.site.register(models.TeamLead)
admin.site.register(models.TeamLeadSocialAccount)
admin.site.register(models.Event)
admin.site.register(models.PhoneNumber)
admin.site.register(models.Member)