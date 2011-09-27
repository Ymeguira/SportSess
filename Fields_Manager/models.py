from django.db import models

# Create your models here.

class Field(models.Model):
    name = models.CharField(max_length=200)
    publisher = models.ForeignKey('Users_Manager.SportSessUser')
    localization = models.CharField(max_length=200)
    sport = models.ForeignKey('Events_Manager.Sport')
    price = models.FloatField()
    material_provided = models.BooleanField()
    
    def __unicode__(self):
        return self.name