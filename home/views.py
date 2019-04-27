from django.shortcuts import render
from bugs.models import Bugs
from features.models import Features
from django.contrib.auth.models import User
from django.http import HttpResponse
import json

# Create your views here.


def all_index(request):
    """This is a  view that displays the index page"""

    return render(request, "index.html", {'index_selected': 'navbar-text-bold'})

def graph(request):
    bugs = Bugs.objects.all()
    features = Features.objects.all()
    users =  User.objects.all()

    t_bugs = bugs.count()
    t_features = features.count()
    t_users =  users.count()

    todos = bugs.filter(status='Todo').count() + features.filter(status='Todo').count()
    pending = bugs.filter(status='Pending').count() + features.filter(status='Pending').count()
    completed = bugs.filter(status='Completed').count() + features.filter(status='Completed').count()

    data = {
        'pie':{
            'label': ['Bugs', 'Features', 'Users'],
            'data': [t_bugs, t_features, t_users],
        },
        'bar':{
            'label': ['Todo', 'Pending', 'Completed'],
            'data': [todos, pending, completed]
        },
    }

    return HttpResponse(json.dumps(data))

def community(request):
    return render(request, 'community.html', {'community_selected': 'navbar-text-bold'})