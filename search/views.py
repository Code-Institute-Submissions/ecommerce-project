from django.shortcuts import render
from bugs.models import Bugs

# Create your views here.

def do_search(request):
    bugs = Bug.objects.filter(name__icontains=request.GET['q'])
    return render(request, "bugs.html", {"bug":bug})