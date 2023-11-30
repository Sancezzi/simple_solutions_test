import stripe

from django.conf import settings


def create_stripe_item_price(item_name: str, currency: str, price: float) -> stripe.Price:
    stripe.api_key = settings.STRIPE_KEYS[currency]['SECRET_KEY']
    
    stripe_item = stripe.Product.create(name=item_name)
    stripe_item_price = stripe.Price.create(
        product=stripe_item['id'],
        unit_amount=round(price * 100),
        currency=currency.lower()
    )
     
    return stripe_item_price
    