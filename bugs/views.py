from django.contrib.auth.decorators import login_required 
from django.shortcuts import render, redirect, get_object_or_404
from .models import Bugs, Comments
from cart.views import cart_items

# Create your views here.

@login_required
def all_bugs(request):
    bugs = Bugs.objects.all().order_by("name") # Sort by created date
    return render(request, "bugs.html", {"bugs": bugs, 'all_bugs': True,"len_items": cart_items(request),"bugs_selected":"navbar-text-bold"})

@login_required
def vote(request, bug_id):
    bug = get_object_or_404(Bugs, pk=bug_id)
    bug.upvotes += 1
    bug.save()
    return redirect("bugs")

@login_required
def delete(request, bug_id):
    bug = get_object_or_404(Bugs, pk=bug_id)
    if bug.author.id == request.user.id:
        bug.delete()
    return redirect("bugs")

@login_required
def comment(request, bug_id):
    bug = get_object_or_404(Bugs, pk=bug_id)
    user_id = request.user
    if request.method == 'POST':
        comment = request.POST['comment']
        comment = Comments.objects.create(
            author=user_id,
            bug_id=bug,
            comment=comment
        )
        return redirect('/bugs/'+str(bug_id))
    return redirect('index')

@login_required
def one_bug(request, bug_id):
    bug = get_object_or_404(Bugs, pk=bug_id)
    comments = Comments.objects.all().filter(bug_id=bug)
    bug.views += 1
    bug.save()
    return render(request, "bug.html", {"bug": bug, "comments": comments})

@login_required
def add_bug(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        img = request.POST['img'] 
        # TODO: Add created Date
        user_id = request.user
        new_bug = Bugs(
            author=user_id,
            name=name,
            description=description,
            price=price,
            image=img)
        new_bug.save()
        return redirect('/bugs/' + str(new_bug.id))
    return render(request, 'add_bug.html')

@login_required
def edit(request, bug_id):
    bug = get_object_or_404(Bugs, pk=bug_id)
    if request.method == 'POST' and bug.author.id == request.user.id:
        bug.name = request.POST['name']
        bug.description = request.POST['description']
        bug.price = request.POST['price']
        bug.image = request.POST['img']
        bug.save()
        return redirect('/bugs/')
    return render(request, 'edit_bug.html', context={'bug': bug})