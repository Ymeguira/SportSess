from django.db import models as dbmodels
from django.contrib.auth import models as authmodels 
import datetime

class Sport(dbmodels.Model):
    name = dbmodels.CharField(max_length=200)
    
    def __unicode__(self):
        return self.name
    
class Event( dbmodels.Model):
    SPORT_DIFFICULTY = (
        (u'B', u'Beginner'),
        (u'I', u'Intermediate'),
        (u'A', u'Advanced'),
    )
    name = dbmodels.CharField(max_length=200)
    publisher = dbmodels.ForeignKey(authmodels.User, related_name="creator")
    publication_date_time = dbmodels.DateTimeField('event published date time', default=datetime.datetime.now())
    sport =  dbmodels.ForeignKey(Sport)
    difficulty = dbmodels.CharField(max_length=2, choices=SPORT_DIFFICULTY)
    date_time = dbmodels.DateTimeField('event date')
    localization = dbmodels.CharField(max_length=200)
    field = dbmodels.ForeignKey('Fields_Manager.Field', blank=True)
    min_number = dbmodels.IntegerField()
    max_number = dbmodels.IntegerField()
    materiel_required = dbmodels.BooleanField()
    subscriber = dbmodels.ManyToManyField(authmodels.User, related_name = "subscriber", blank=True)
    comment = dbmodels.CharField(max_length=1000, blank=True)
    
    def addSubscriber(self, event_subscriber):
        if len(self.subscriber) < self.max_number:
           self.subscriber += event_subsriber
           
    def removeSubscriber(self, event_subscriber):
        self.subscriber -= event_subscriber
    
    def __unicode__(self):
        return self.name
    
