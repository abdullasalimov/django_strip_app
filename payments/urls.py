from django.urls import path
from .views import (
    CreateCheckoutSessionView, 
    ItemListPageView, 
    SuccessView, 
    CancelView, 
    ItemDetailPageView, 
    ItemCreateView
    )

urlpatterns = [
    path('', ItemListPageView.as_view(), name='home'),
    path('buy/<int:pk>/', CreateCheckoutSessionView.as_view(), name='buy'),
    path('item/<int:pk>/', ItemDetailPageView.as_view(), name='detail'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
    path('create/', ItemCreateView.as_view(), name='create'),
]