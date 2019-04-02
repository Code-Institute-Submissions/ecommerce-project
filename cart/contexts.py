from django.shortcuts import get_object_or_404
from bugs.models import Bugs


def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering every page
    """
    
    cart = request.session.get('cart', {})
    
    cart_items = []
    total = 0
    bugs_count = 0
    for id, quantity in cart.items():
        bugs = get_object_or_404(Bugs, pk=id)
        total += quantity * bugs.price
        bugs_count += quantity
        cart_items.append({'id':id, 'quantity': quantity, 'bug': bugs})
        
    return { 'cart_items': cart_items, 'total': total, 'bug_count': bugs_count }
