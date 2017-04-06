from __future__ import unicode_literals
from django.db import models
import django


# Create your models here.

class Scrum(models.Model): #TODO: ownership
    comp_yest = models.TextField(max_length=500 )
    roadblk = models.CharField(max_length=500,blank=True)
    plan_tdy = models.CharField(max_length=500)
    learning = models.CharField(max_length=500,blank=True)
    date = models.DateField(default='2011-11-11')
    created_by = models.CharField(max_length=50)

    def __str__(self):
        return self.created_by + " " + str(self.date)


class SessionReq(models.Model):
    SessionOn = models.CharField(max_length=30)
    Details = models.CharField(max_length=200, blank=True)
    project = models.CharField(max_length=20)
    date = models.DateField(default='2011-11-11')

    def __str__(self):
        return self.SessionOn + " " + str(self.date)

class synthesis(models.Model):
    heading = models.CharField(max_length=30)
    content = models.TextField(max_length=1000)
    source = models.URLField()
    by = models.CharField(max_length= 15)

    def __str__(self):
        return self.heading[0:14]