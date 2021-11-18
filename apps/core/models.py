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
    email = models.EmailField()
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


class Event(models.Model):
    """
    This models stores info all events
    """
    OPTIONS = (
        ('meeting', 'Meeting'),
        ('workshop', 'Workshop'),
        ('seminar', 'Seminar'),
    )
    title = models.CharField(max_length=200)
    poster = models.ImageField()
    location = models.CharField(max_length=200)
    date_time = models.DateTimeField()
    duration = models.DurationField(blank=True)
    info = models.TextField(help_text="more helpful informations...")

    def __str__(self) -> str:
        return self.title


class FAQ(models.Model):
    """
    This model stores all Frequently Asked Questions
    """
    site = models.ForeignKey(
        Site, related_name='faqs', on_delete=models.CASCADE)
    question = models.CharField(max_length=200)
    answer = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.question


class TeamLead(models.Model):
    """
    This model stores all infomations about each team leads
    """
    site = models.ForeignKey(
        Site, related_name='team_leads', on_delete=models.CASCADE)
    fullname = models.CharField(max_length=60)
    title = models.CharField(max_length=100, help_text='position occupied')
    photo = models.ImageField()
    blockquote = models.TextField(
        help_text="your favourite quote or whatever you feel...")

    def __str__(self) -> str:
        return self.fullname


class SocialAccount(models.Model):
    OPTIONS = (
        ('facebook', 'Facebook'),
        ('instagram', 'Instagram'),
        ('linkedin', 'LinkedIn'),
        ('twitter', 'Twitter'),
    )
    name = models.CharField(max_length=20, choices=OPTIONS)
    url = models.URLField()

    def __str__(self) -> str:
        return self.name


class SiteSocialAccount(SocialAccount):
    site = models.ForeignKey(
        Site, related_name='social_accounts', on_delete=models.CASCADE)


class TeamLeadSocialAccount(SocialAccount):
    site = models.ForeignKey(
        TeamLead, related_name='social_accounts', on_delete=models.CASCADE)


class Member(models.Model):
    """
    This models stores the members info for the 
    passport.
    """
    DEPARTMENT_OPTIONS = (
        ('civil engr', 'Civil Engineering'),
        ('mech engr', 'Mechanical Engineering'),
        ('elect engr', 'Electrical Engineering'),
        ('Computer engr', 'Computer Engineering'),
    )
    TEAM_OPTIONS = (
        ('0','Media Team'),
        ('1', 'Research Team'),
        ('2', 'Logistics Team'),
        ('3','Project Supervision Team'),
        ('4', 'Finance Team'),
        ('5', 'Departmental Team'),
        ('6','Design and Creative Team'),
        ('7','Purchase Team'),
        ('8', 'Organizing Team'),
        ('9', 'Project Team'),
        ('10', 'Campus Team'),
    )
    
    lastname = models.CharField(
        max_length=100, help_text='Your surname')
    firstname = models.CharField(
        max_length=100, help_text='Your name')
    othername = models.CharField(
        max_length=100, help_text="Your middle name"
    )
    department = models.CharField(max_length=50, choices=DEPARTMENT_OPTIONS)
    position = models.CharField(max_length=50, default='Nil')
    team = models.CharField(max_length=30, choices=TEAM_OPTIONS)
    passport = models.ImageField(help_text='Strictly your pasport photograph on a white background')

    def __str__(self) -> str:
        return  self.get_fullname()

    def get_fullname(self):
        return f"{self.lastname} {self.firstname} {self.othername}".title()
