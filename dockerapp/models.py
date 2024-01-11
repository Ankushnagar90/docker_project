from django.db import models

# Create your models here.

class Sum(models.Model):
    var1 = models.IntegerField(default=0)
    var2 = models.IntegerField(default=0)
