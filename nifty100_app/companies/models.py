from django.db import models

class Company(models.Model):
    symbol = models.CharField(max_length=20, primary_key=True)
    company_name = models.CharField(max_length=200)
    sector = models.CharField(max_length=100)
    website = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return self.company_name
