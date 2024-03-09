from django.db import models

class Demon(models.Model):
    name = models.CharField(verbose_name= "Name", max_length=25)
    race = models.CharField(verbose_name= "race", max_length=5, blank=True, null=True) #human or demon
    affiliation = models.CharField(verbose_name= "affiliation", max_length=100, blank=True, null=True)
    skill = models.CharField(verbose_name= "skill", max_length=100, blank=True, null=True)
    quote = models.CharField(verbose_name= "quote", max_length=255, blank=True, null=True)