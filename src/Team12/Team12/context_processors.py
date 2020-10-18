from cart.models import Cart, LineItem

def cart(request):
    try:
        cart = Cart.objects.get(web_user=request.user)
        cart_items = LineItem.objects.filter(cart=cart) if cart else None
    except:
        cart = None
        cart_items = None
        
    return {
        'cart': cart,
        'cart_items': cart_items
    }
