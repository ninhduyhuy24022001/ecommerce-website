from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .cart import Cart
from product.models import Product

def cart(request):
    cart = Cart(request)

    return render(request, 'cart/cart.html')

def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)

    return render(request, 'cart/partials/menu_cart.html')

def update_cart(request, product_id, action):
    cart = Cart(request)

    if action == "increment":
        cart.add(product_id, 1, True)
    else:
        cart.add(product_id, -1, True)
    
    product = Product.objects.get(pk=product_id)
    quantity = cart.get_item(product_id)

    if quantity:
        quantity = quantity['quantity']

        item = {
            'product': {
                'id': product.id,
                'name': product.name,
                'image': product.image,
                'slug': product.slug,
                'get_thumbnail': product.get_thumbnail(),
                'price': product.price
            },
            'total_price': (quantity * product.price),
            'quantity': quantity,
        }
    else:
        item = None

    response = render(request, 'cart/partials/cart_item.html', {'item': item})
    response['HX-Trigger'] = 'update-menu-cart'

    return response
    
def hx_menu_cart(request):
    return render(request, 'cart/partials/menu_cart.html')

def hx_cart_total(request):
    return render(request, 'cart/partials/cart_total.html')

def hx_checkout_button(request):
    return render(request, 'cart/partials/hx_checkout_button.html')

@login_required 
def checkout(request):
    return render(request, 'cart/checkout.html')