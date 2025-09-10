from django.db import models
from django.contrib.auth.models import User

class Holding(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stock_symbol = models.CharField(max_length=10)
    quantity = models.PositiveIntegerField()
    purchase_price = models.FloatField()
    purchase_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.stock_symbol}"
