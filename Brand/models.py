from django.db import models


# Create your models here.

class Brand(models.Model):
    title = models.CharField(max_length=50, verbose_name="brand")

    created_time = models.DateTimeField(auto_created=True)
    modified_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
