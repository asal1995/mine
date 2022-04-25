from django.db import models


class Appointment(models.Model):
    brand = models.ForeignKey("Brand", on_delete=models.CASCADE, related_name="brand")
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="customer"
    )
    created_time = models.DateTimeField(auto_created=True)
    modified_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer.username}"

     