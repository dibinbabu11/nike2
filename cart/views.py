from django.shortcuts import render,redirect
from nike_app .models import Nikeshoe
from . models import Cart,CartItem
from django .core.exceptions import ObjectDoesNotExist
# Create your views here.
def cart_id(request):
    cart=request.session.session_key
    if not cart:
        cart=request.session.create()
    return cart


def add_cart(request,nikeshoe_id):
    nikeshoe=Nikeshoe.objects.get(id=nikeshoe_id)
    try:
        cart=Cart.objects.get(cart_id=cart_id(request))
    except Cart.DoesNotExist:
        cart=Cart.objects.create(cart_id=cart_id(request))
        cart.save()

    try:
        cart_item=CartItem.objects.get(nikeshoe=nikeshoe,cart=cart)
        if cart_item.quantity < cart_item.nikeshoe.stock:
            cart_item.quantity +=1

        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item=CartItem.objects.create(nikeshoe=nikeshoe,quantity=1,cart=cart)
        cart_item.save()
    return redirect('cart:cart_detail')
def cart_deatil(request,total=0,counter=0,cart_item=None):
    try:
        cart=Cart.objects.get(cart_id=cart_id(request))
        cart_item=CartItem.objects.filter(cart=cart,active=True)
        for cartitem in cart_item:
            total += (cartitem.nikeshoe.price * cartitem.quantity)
            counter +=cartitem.quantity
    except ObjectDoesNotExist:
        pass
    return render(request,"cart.html",{'cart_item':cart_item,'total':total,'counter':counter})

