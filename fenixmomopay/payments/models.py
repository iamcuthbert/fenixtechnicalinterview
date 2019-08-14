from django.db import models


class MomoRequest(models.Model):
    amount = models.IntegerField()
    currency = models.CharField(max_length='3')
    externalId = models.IntegerField()
    payee = models.CharField(max_length=255)
    payerMessage = models.CharField(max_length=500)
    payeeNote = models.CharField(max_length=500)
    status = models.CharField(max_length=10)
