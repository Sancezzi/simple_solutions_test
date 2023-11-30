from django.urls import path

from items.views import ItemView, CancelView, SuccessView, ItemBuyView

app_name = 'items'

urlpatterns = [
    path('item/<int:id>/', ItemView.as_view(), name='item'),
    path('buy/<int:id>/', ItemBuyView.as_view(), name='buy'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success')
]
