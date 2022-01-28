from django.db import models

class Continents(models.Model):
    continent_de = models.CharField(max_length=20, blank=True)
    continent_en = models.CharField(max_length=20, blank=True)
    continent_sr = models.CharField(max_length=20)

    def __str__(self):
        return self.continent_sr

        

