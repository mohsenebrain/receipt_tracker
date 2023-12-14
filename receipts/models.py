from django.db import models
from django.contrib.auth.models import User

class Receipt(models.Model):

    name = models.CharField(max_length=100)
    date_purchase = models.DateField(verbose_name="Date of purchase")
    item_list = models.TextField(verbose_name="list item")
    total_amount = models.DecimalField(verbose_name="total amount",max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.date_purchase}"
