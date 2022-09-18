from django.urls import path
from .views import (
    create_checkout_session, 
    ItemListPageView, 
    SuccessView, 
    CancelView, 
    ItemDetailPageView, 
    ItemCreateView
    )

urlpatterns = [
    path('', ItemListPageView.as_view(), name='item'),
    path('item/<int:id>/', ItemDetailPageView.as_view(), name='item_detail'),
    path('buy/<int:id>/', create_checkout_session, name='buy'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
    path('create/', ItemCreateView.as_view(), name='create'),
]