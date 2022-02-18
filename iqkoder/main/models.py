from django.db import models

class Continents(models.Model):
    continent_de = models.CharField(max_length=20, blank=True)
    continent_en = models.CharField(max_length=20, blank=True)
    continent_sr = models.CharField(max_length=20)

    def __str__(self):
        return self.continent_sr

class Countries(models.Model):
    country_de = models.CharField(max_length=50, blank=True)
    country_en = models.CharField(max_length=50, blank=True)
    country_sr = models.CharField(max_length=50)
    continent = models.ForeignKey(Continents, blank=True, null=True, on_delete=models.CASCADE)
    flag = models.ImageField(blank=True, null=True, upload_to='countries/')

    def __str__(self):
        return self.country_sr

        

