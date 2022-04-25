from django.db import models


# Create your models here.
class Bid(models.Model):
    price = models.IntegerField(default=1)
    bider = models.ForeignKey(Bider, on_delete=models.CASCADE, related_name="bider")
    auction = models.ForeignKey("Auction", on_delete=models.CASCADE, related_name="winner")
    created_time = models.DateTimeField(auto_created=True)
    modified_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.bider}"
