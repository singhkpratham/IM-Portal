from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from accounts.models import Project, Product
from datetime import  datetime


# Create your models here.

class Scrum(models.Model):
    comp_yest = models.TextField(max_length=500 )
    roadblk = models.CharField(max_length=500,blank=True, verbose_name='RoadBlocks if any')
    plan_tdy = models.CharField(max_length=500)
    learning = models.CharField(max_length=500,blank=True)
    date = models.DateField(default='2011-11-11')
    created_by = models.CharField(max_length=50)
    project = models.ForeignKey(Project, blank=True, null=True)

    def __str__(self):
        return self.created_by + " " + str(self.date)


class SessionReq(models.Model):
    SessionOn = models.CharField(max_length=30)
    Details = models.CharField(max_length=200, blank=True)
    project = models.ForeignKey(Project)
    date = models.DateField(default='2011-11-11')
    votes = models.ManyToManyField(User,limit_choices_to={'groups__name': 'ironmen'}, blank=True)

    class Meta:
        ordering = ['-date']
        verbose_name = "Requested Session"

    def __str__(self):
        return self.SessionOn + " " + str(self.date) + " " + str(self.votes.count())

class synthesis(models.Model):
    heading = models.CharField(max_length=30)
    content = models.TextField(max_length=1000)
    source = models.URLField()
    by = models.CharField(max_length= 15)
    team = models.ForeignKey(User)
    time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.heading[0:14]

class Bug(models.Model):
    txt = models.TextField("Enter Bug/Request",default='')
    que = models.BooleanField("Bug?" , default=True)
    team  = models.ForeignKey(User)
    prod = models.ForeignKey(Product)
    time = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return  ('Bug ' if self.que else 'Feature ') + (self.txt[0:15])

class ShareDoc(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    team = models.ForeignKey(User)
    project = models.ForeignKey(Project)
    time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return str(self.team) + str(self.project) + self.text[1:15]

    class Meta:
        ordering = ['-time']
        verbose_name = "Shared Files"