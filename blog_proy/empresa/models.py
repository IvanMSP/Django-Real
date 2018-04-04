# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Empresa(models.Model):
    name = models.CharField(max_length=250, blank=True , null = True)
    adress = models.CharField(max_length= 250, blank=True, null=True)
    logo = models.ImageField(upload_to='images-empresas', blank=True, null=True)


    def __str__(self):
        return self.name

