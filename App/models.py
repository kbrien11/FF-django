from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Quarterback(models.Model):
    name = models.CharField(max_length=100,blank=False)
    team = models.CharField(max_length=32)
    position = models.CharField(max_length=3, blank=False)
    Bye_Week = models.CharField(max_length=10,default=0)
    Passing_yards = models.IntegerField(default=0)
    Passing_TD = models.IntegerField(default=0)
    INT = models.IntegerField(default=0)
    Rush_Yards = models.IntegerField(default=0)
    Rush_TD = models.IntegerField(default=0)
    FPTS = models.IntegerField(default=0)
    Projected_Passing_yards = models.IntegerField(default=0)
    Projected_Passing_TD = models.IntegerField(default=0)
    Projected_INT = models.IntegerField(default=0)
    Projected_Rush_Yards = models.IntegerField(default=0)
    Projected_Rush_TD = models.IntegerField(default=0)
    Projected_FPTS = models.IntegerField(default=0)
    Projected_OUTLOOK = models.TextField(default='None')

class Runningback(models.Model):
    name = models.CharField(max_length=100, blank=False)
    team = models.CharField(max_length=32)
    position = models.CharField(max_length=3, blank=False)
    bye_week = models.CharField(max_length=10, default=0)
    rush_yards = models.IntegerField(default=0)
    rush_td = models.IntegerField(default=0)
    receptions = models.IntegerField(default=0)
    rec_yards = models.IntegerField(default=0)
    rec_td = models.IntegerField(default=0)
    total_yards = models.IntegerField(default=0)
    total_td = models.IntegerField(default=0)
    fpts = models.FloatField(default=0)
    projected_rush_yards = models.IntegerField(default=0)
    projected_rush_td = models.IntegerField(default=0)
    projected_receptions = models.IntegerField(default=0)
    projected_rec_yards = models.IntegerField(default=0)
    projected_rec_td = models.IntegerField(default=0)
    projected_total_yards = models.IntegerField(default=0)
    projected_total_td = models.IntegerField(default=0)
    projected_fpts = models.FloatField(default=0)
    projected_OUTLOOK = models.TextField(default='None')


class Widereceiver(models.Model):
    name = models.CharField(max_length=100, blank=False)
    team = models.CharField(max_length=32)
    position = models.CharField(max_length=3, blank=False)
    bye_week = models.CharField(max_length=10, default=0)
    targets = models.IntegerField(default=0)
    receptions = models.IntegerField(default=0)
    rec_yards = models.IntegerField(default=0)
    rec_td = models.IntegerField(default=0)
    fpts = models.FloatField(default=0)
    projected_targets = models.IntegerField(default=0)
    projected_receptions = models.IntegerField(default=0)
    projected_rec_yards = models.IntegerField(default=0)
    projected_rec_td = models.IntegerField(default=0)
    projected_fpts = models.FloatField(default=0)
    projected_OUTLOOK = models.TextField(default='None')

class Tightend(models.Model):
    name = models.CharField(max_length=100, blank=False)
    team = models.CharField(max_length=32)
    position = models.CharField(max_length=3, blank=False)
    bye_week = models.CharField(max_length=10, default=0)
    targets = models.IntegerField(default=0)
    receptions = models.IntegerField(default=0)
    rec_yards = models.IntegerField(default=0)
    rec_td = models.IntegerField(default=0)
    fpts = models.FloatField(default=0)
    projected_targets = models.IntegerField(default=0)
    projected_receptions = models.IntegerField(default=0)
    projected_rec_yards = models.IntegerField(default=0)
    projected_rec_td = models.IntegerField(default=0)
    projected_fpts = models.FloatField(default=0)
    projected_OUTLOOK = models.TextField(default='None')

class Defense(models.Model):
    team = models.CharField(max_length=32)
    bye_week = models.CharField(max_length=10)
    sacks = models.IntegerField(default=0)
    turnovers = models.IntegerField()
    td = models.IntegerField()
    fpts = models.IntegerField()
    projected_sacks = models.IntegerField()
    projected_turnovers = models.IntegerField()
    projected_td = models.IntegerField()
    projected_fpts = models.IntegerField()
    projected_OUTLOOK = models.TextField(default="None")

class Kicker(models.Model):
    name = models.CharField(max_length=100, blank=False)
    team = models.CharField(max_length=32)
    position = models.CharField(max_length=3, blank=False)
    bye_week = models.CharField(max_length=10, default=0)
    total_made_fg = models.IntegerField(default=0)
    fpts = models.IntegerField(default=0)
    projected_total_made_fg = models.IntegerField(default=0)
    projected_fpts = models.IntegerField(default=0)
    projected_OUTLOOK = models.TextField(default=None)

class Player(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100, blank=False)
    team = models.CharField(max_length=32)
    position = models.CharField(max_length=3, blank=False)
    bye_week = models.CharField(max_length=10, default=0)
    is_drafted = models.BooleanField(default=False,null=True)








