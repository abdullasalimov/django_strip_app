from django.conf import settings
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (
    TemplateView, 
    DetailView, 
    ListView, 
    CreateView)

import stripe

from .models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY

class SuccessView(TemplateView):
    template_name = "success.html"

class CancelView(TemplateView):
    template_name = "cancel.html"

class ItemListPageView(ListView):
    model = Item
    template_name = 'item.html'
    context_object_name = 'items'

class ItemDetailPageView(DetailView):
    model = Item
    template_name = 'item_detail.html'
    pk_url_kwarg = 'pk'

class ItemCreateView(CreateView):
    model = Item
    fields = '__all__'
    template_name = "create.html"
    success_url = reverse_lazy("item")
    

class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        item_id = self.kwargs["pk"]
        item = get_object_or_404(Item, pk=item_id)

        product = stripe.Product.create(name=item.name)
        price = stripe.Price.create(product=product, unit_amount=item.price, currency=item.currency)

        checkout_session = stripe.checkout.Session.create(
            line_item=[
                {
                    'price':price,
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=settings.DOMAIN + '/success/',
            cancel_url=settings.DOMAIN + '/cancel/',
        )
        return redirect(checkout_session.url, code=303)