from django.urls import path
from . import views
app_name='cart'

urlpatterns = [
    path('add/<int:nikeshoe_id>/',views.add_cart,name='add_cart'),
    path('cart_detail/',views.cart_deatil, name="cart_detail"),
]