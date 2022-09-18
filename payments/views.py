from django.conf import settings
from django.http.response import JsonResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy, reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import (
    TemplateView, 
    DetailView, 
    ListView, 
    CreateView
    )

import stripe

from payments.models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY


class ItemListPageView(ListView):
    model = Item
    template_name = 'item.html'
    context_object_name = 'items'

class ItemDetailPageView(DetailView):
    model = Item
    template_name = 'item_detail.html'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super(ItemDetailPageView, self).get_context_data(**kwargs)
        context['stripe_public_key'] = settings.STRIPE_PUBLIC_KEY
        return context  

class ItemCreateView(CreateView):
    model = Item
    fields = '__all__'
    template_name = "create.html"
    success_url = reverse_lazy("item")
    
@csrf_exempt
def create_checkout_session(request, id):
    item = get_object_or_404(Item, pk=id)

    stripe.api_key = settings.STRIPE_SECRET_KEY

    product = stripe.Product.create(name=item.name)
    price = stripe.Price.create(product=product, unit_amount=item.price, currency=item.currency)
    
    checkout_session = stripe.checkout.Session.create(
        line_items=[
            {
                "price": price,
                "quantity": 1,
            }
        ],
        mode="payment",
        success_url=request.build_absolute_uri(
            reverse('success')
        ) + "?session_id={CHECKOUT_SESSION_ID}",
        cancel_url=request.build_absolute_uri(reverse('cancel')),

    )

    return JsonResponse({'sessionId': checkout_session.id})

class SuccessView(TemplateView):
    template_name = "success.html"

    def get(self, request, *args, **kwargs):
        session_id = request.GET.get('session_id')
        if session_id is None:
            return HttpResponseNotFound()
            
        stripe.api_key = settings.STRIPE_SECRET_KEY

        return render(request, self.template_name)


class CancelView(TemplateView):
    template_name = "cancel.html"