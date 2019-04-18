from django.shortcuts import render, redirect, get_object_or_404
from .models import Features, FeatureComments

# Create your views here.


def all_features(request):
    features = Features.objects.all()
    return render(request, "features.html", {'features': features})


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

        return redirect("/features/"+str(feature_id))
    return redirect('index')


def one_feature(request, feature_id):
    feature = get_object_or_404(Features, pk=feature_id)
    comments = FeatureComments.objects.all().filter(features=feature)
    return render(request, "feature.html", {
        "feature": feature, "comments": comments})


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
        return redirect('/features/'+str(new_feature.id))
    return render(request, 'add_feature.html')
