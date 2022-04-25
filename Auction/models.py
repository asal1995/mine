from django.db import models


# Create your models here.
class Auction(models.Model):
    start_price = models.PositiveBigIntegerField()
    inspection = models.ForeignKey("Inspection", on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_created=True)
    modified_time = models.DateTimeField(auto_now_add=True)
