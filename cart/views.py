import stripe

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse, get_object_or_404
from cart.models import Cart
from features.models import Features
from django.conf import settings


def cart_items(request):
    if request.user:
        cart = Cart.objects.filter(user=request.user).get()
        return len(cart.features_set.all())
    return None


@login_required
def view_cart(request):
    """A view that renders the cart contents page"""
    Cart.objects.create(user=request.user).save()
    cart = Cart.objects.filter(user=request.user).get()
    features = cart.features_set.all()
    amt = len(features) * 5
    total = amt * 100
    len_items = len(features)
    key = settings.STRIPE_PUBLISHABLE
    return render(request, "mycart.html", context={"items": features, "total": total, "amt": amt, "len_items": len_items, "key": key})


@login_required
def del_cart_item(request, item_id):
    cart = Cart.objects.filter(user=request.user).get()
    feature = get_object_or_404(Features, pk=item_id)
    if cart.user.id == request.user.id:
        feature.cart.remove(cart)
    return redirect("view_cart")


@login_required
def charge(request, total):
    cart = Cart.objects.filter(user=request.user).get()
    if request.method == 'POST':
        stripe.Charge.create(
            amount=total,
            currency='euro',
            description='Noelle ECommerce',
            source=request.POST['stripeToken']
        )
        cart.features_set.clear()
        features = cart.features_set.all()
        total = len(features) * 5
        return render(request, 'charge.html', context={"items": features, "total": total, "len_items": cart_items(request)})
    return redirect('view_cart')


@login_required
def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    return redirect(reverse('index'))


@login_required
def adjust_cart(request, id):
    """Adjust the quantity of the specified product to the specified amount"""
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
    