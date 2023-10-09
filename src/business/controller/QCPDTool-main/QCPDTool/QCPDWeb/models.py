'''Module for defining the Django ORM Model for DB management/abstraction'''
from django.db import models

# Create your models here.
class Pattern(models.Model):
    '''Pattern Abstract model for Django ORM'''
    name = models.CharField(max_length=200, unique=True)
    desc = models.CharField(max_length=1000, default='Quantum Circuit Design Pattern')
    json = models.CharField(max_length=10000)
    xml = models.CharField(max_length=10000)
    url = models.CharField(max_length=1000, default='https://www.quantumcomputingpatterns.org/#/')

    def __str__(self):
        return f'{self.name}: {self.desc}\n\tJSON: ' +\
            '{self.json}\n\tXML: {self.xml}\n\tURL: {self.url}'
