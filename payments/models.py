from django.db import models


class Item(models.Model):
    CURRENCY = (("usd", "usd"), ("eur", "eur"))
    
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    price = models.IntegerField(default=50)
    currency = models.CharField(max_length=3, choices=CURRENCY, blank=False, default='usd')
    
    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)


    def __str__(self):
        return self.name