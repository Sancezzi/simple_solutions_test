from django.db import models

from items.stripe import create_stripe_item_price

# Create your models here.
class Item(models.Model):
    class Currencies(models.TextChoices):
        CURRENCY_1 = 'RUB', 'RUB'
        CURRENCY_2 = 'USD', 'USD'
    
    name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.DecimalField(max_digits=15, decimal_places=2)
    currency = models.CharField(max_length=3, choices=Currencies.choices, default=Currencies.CURRENCY_2)
    stripe_item_price_id = models.CharField(max_length=256, blank=True, null=True)
    
    def save(self, *args, **kwargs):
        if not self.stripe_item_price_id:
            stripe_item_price = create_stripe_item_price(
                item_name=self.name, 
                currency=self.currency, 
                price=self.price
                )
            self.stripe_item_price_id = stripe_item_price['id']
    
        super().save(*args, **kwargs)
        
    
    def __str__(self):
        return self.name

    