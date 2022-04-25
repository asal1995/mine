from django.db import models


# Create your models here.
class Inspection(models.Model):
    INS_STATUS = [("Under inspection", "Under inspection"), ("inspected", "inspected")]
    status = models.CharField(max_length=50, choices=INS_STATUS, verbose_name="status")

    appointmet = models.ForeignKey(
        "Appointment", on_delete=models.CASCADE, related_name="appointment"
    )

    created_time = models.DateTimeField(auto_created=True)
    modified_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.status}"
