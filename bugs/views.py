from django.shortcuts import render, redirect, get_object_or_404
from .models import Bugs, Comments

# Create your views here.


def all_bugs(request):
    bugs = Bugs.objects.all()
    return render(request, "bugs.html", {"bugs": bugs})


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


def one_bug(request, bug_id):
    bug = get_object_or_404(Bugs, pk=bug_id)
    comments = Comments.objects.all().filter(bug_id=bug)
    return render(request, "bug.html", {"bug": bug, "comments": comments})


def add_bug(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        img = request.POST['img']
        user_id = request.user
        new_bug = Bugs(
            author=user_id,
            name=name,
            description=description,
            price=price,
            image=img)
        new_bug.save()
        return redirect('/bugs/'+str(new_bug.id))
    return render(request, 'add_bug.html')
