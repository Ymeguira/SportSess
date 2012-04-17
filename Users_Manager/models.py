from django.contrib.auth import models as authmodels
from django.db import models as dbmodels
from django.utils import encoding
from datetime import date
from django.db.models.signals import post_save

# Create your models here.

class SportSessUser(dbmodels.Model):
    
    user = dbmodels.OneToOneField(authmodels.User, default=authmodels.AnonymousUser())
    
    USER_GENDER = (
        ('M', ('Male')),
        ('F', ('Female')),
    )
    
    ACTIVE_STATUS = 1
    DEACTIVE_STATUS = 2
    ARCHIVE_STATUS = 3
    STATUS_CHOICES = (
        (ACTIVE_STATUS, ('Active')),
        (DEACTIVE_STATUS, ('Deactive')),
        (ARCHIVE_STATUS, ('Archived')),
    )
    
    birthday = dbmodels.DateField()
    status = dbmodels.IntegerField(choices=STATUS_CHOICES, default=ACTIVE_STATUS, max_length=1)
    gender= dbmodels.CharField(max_length=4, choices=USER_GENDER)
    friends = dbmodels.ManyToManyField("self", blank=True)
    location = dbmodels.CharField(max_length=200, blank=True)
    sports = dbmodels.ManyToManyField('Events_Manager.Sport', blank=True)
    professionnal = dbmodels.BooleanField(default=False)        
    
    def __init__(self, *args, **kwargs):
        
        super(SportSessUser, self).__init__(*args, **kwargs) 
        
        related_user = kwargs.get('user')
        if related_user != None:
            self.user = related_user
            
        self.gender = kwargs.get('gender','M')
        self.birthdate = kwargs.get('birthday','')
        
        
    def __unicode__(self):
        return self.user.username or "Anonymous"
    
    def get_age(self):
        age = date.today().year - self.birthday.year
        try:
            anniversary = self.birthday.replace(year=date.today().year)
        except ValueError:
            assert self.birthday.day == 29 and self.birthday.month == 2
            if leap_day_anniversary_Feb28:
                anniversary = date(date.today().year, 2, 28)
            else:
                anniversary = date(date.today().year, 3, 1)
        if date.today() < anniversary:
            age -= 1
        return age 
    
    def get_username(self):
        return self.user.username
    
    def get_last_name(self):
        return self.user.last_name
    
    def get_first_name(self):
        return self.user.first_name
    
    def get_email(self):
        return self.user.email
    
"""   
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        SportSessUser.objects.create(user=instance)

post_save.connect(create_user_profile, sender=authmodels.User)
"""
    
    
  
    
        
        
        
        