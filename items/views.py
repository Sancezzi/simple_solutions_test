import stripe

from django.conf import settings
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic.base import TemplateView
from django.urls import reverse

from items.models import Item


class ItemView(View):
    def get(self, request, id):
        item = get_object_or_404(Item, id=id)
        template = loader.get_template('items/item.html')
        stripe_pub_key = settings.STRIPE_KEYS[item.currency]['PUB_KEY']
        context = {'item': item, 'stripe_pub_key': stripe_pub_key}
        return HttpResponse(template.render(context, request))


class ItemBuyView(View):
    def get(self, request, id):
        item = get_object_or_404(Item, id=id)
        stripe.api_key = settings.STRIPE_KEYS[item.currency]['SECRET_KEY']
        price = item.stripe_item_price_id

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price': price,
                'quantity': 1,
            }],
            mode='payment',
            success_url=request.build_absolute_uri(reverse('items:success')),
            cancel_url=request.build_absolute_uri(reverse('items:cancel')),
        )
        return HttpResponse(checkout_session.id)


class SuccessView(TemplateView):
    template_name = 'items/success.html'


class CancelView(TemplateView):
    template_name = 'items/cancel.html'
