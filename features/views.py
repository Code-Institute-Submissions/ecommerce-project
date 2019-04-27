from django.contrib.auth.decorators import login_required 
from django.shortcuts import render, redirect, get_object_or_404
from .models import Features, FeatureComments
from cart.models import Cart
from cart.views import cart_items


@login_required
def all_features(request): 
    features = Features.objects.all().order_by("description") # date/time
    return render(request, "features.html", {
        'features': features,
        'all_features': True,
        "len_items": cart_items(request),
        "features_selected":"navbar-text-bold",
        'bg_img':'background-image'
        })


@login_required
def vote(request, feature_id):
    feature = get_object_or_404(Features, pk=feature_id)
    cart = Cart.objects.get(user=request.user)
    feature.upvotes += 1
    feature.cart.add(cart)
    feature.save()
    return redirect("features")


@login_required
def delete(request, feature_id):
    feature = get_object_or_404(Features, pk=feature_id)
    if feature.user.id == request.user.id:
        feature.delete()
    return redirect("features")


@login_required
def comment(request, feature_id):
    features = get_object_or_404(Features, pk=feature_id)
    user_id = request.user
    if request.method == 'POST':
        comment = request.POST['comment']
        comment = FeatureComments.objects.create(
            user=user_id,
            features=features,
            comments=comment
        )

        return redirect("/features/" + str(feature_id))
    return redirect('index')


@login_required
def one_feature(request, feature_id):
    feature = get_object_or_404(Features, pk=feature_id)
    comments = FeatureComments.objects.all().filter(features=feature)
    feature.views += 1
    feature.save()
    return render(request, "feature.html", {
        "feature": feature, "comments": comments, "len_items": cart_items(request)})


@login_required
def add_feature(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        price_of_feature = request.POST['price']
        user_id = request.user
        new_feature = Features(
            user=user_id,
            title=title,
            description=description,
            price_of_feature=price_of_feature)
        new_feature.save()
        return redirect('/features/' + str(new_feature.id))
    return render(request, 'add_feature.html')


@login_required
def edit(request, feature_id):
    feature = get_object_or_404(Features, pk=feature_id)
    if request.method == 'POST' and feature.user.id == request.user.id:
        feature.title = request.POST['title']
        feature.description = request.POST['description']
        feature.price_of_feature = request.POST['price']
        feature.save()
        return redirect('/features/')
    return render(request, 'edit_feature.html', context={'feature': feature})
