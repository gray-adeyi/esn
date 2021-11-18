from django.contrib import admin
from . import models

admin.AdminSite.site_header = "ESN Website Administration"
admin.AdminSite.index_title = "With great power, comes great responsibility"

# Register your models here.
admin.site.register(models.Event)


class PhoneNumberInline(admin.TabularInline):
    model = models.PhoneNumber
    extra = 1


class FAQInline(admin.TabularInline):
    model = models.FAQ
    extra = 2


class TeamLeadInline(admin.TabularInline):
    model = models.TeamLead
    extra = 1


class SiteSocialAccountInline(admin.TabularInline):
    model = models.SiteSocialAccount
    extra = 2


class TeamLeadSocialAccountInline(admin.TabularInline):
    model = models.TeamLeadSocialAccount
    extra = 1


@admin.register(models.Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [
        TeamLeadInline,
        PhoneNumberInline,
        FAQInline,
        SiteSocialAccountInline,

    ]

    fieldsets = [
        ('Website Informations', {'fields': [
            'name',
            'domain',
            'about',
            'mission',
            'vision',
            'favicon',
            'appleicon',
            'logo',
            'email',
            'address'
        ]}),
    ]


@admin.register(models.TeamLead)
class TeamLeadAdmin(admin.ModelAdmin):
    inlines = [
        TeamLeadSocialAccountInline
    ]


@admin.register(models.Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'department', 'team']
    list_filter = ['department', 'team']

    def fullname(self, obj):
        return obj.get_fullname()
