from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Payment(models.Model):
    STATUS = (
    ("PENDING", "Pending"),
    ("SUCCESS", "Success"),
    ("FAILED", "Failed")
    )
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    house_address = models.CharField(max_length=10)
    amount_sent  = models.DecimalField(decimal_places=3, max_digits=3)
    network = models.CharField(max_length=15, default="MTN")
    Number = models.IntegerField(default="+233XXXXXXXXX")
    location = models.CharField(max_length=25, default="GARU")
    Date   = models.DateTimeField(auto_now_add=True)
    Description = models.TextField(null=True, blank=True)
    Transaction_Details = models.TextField()
    Accepted = models.CharField(max_length=15, default="Pending", choices=STATUS)
