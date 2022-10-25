from django.db import models

class Thing(models.Model):
    name = models.CharField(
    max_length = 30
    unique = True
    )

    description = models.CharField(
    max_length = 120
    blank = False
    )

    quantity = models.IntegerField(
    max_value = 100
    )
