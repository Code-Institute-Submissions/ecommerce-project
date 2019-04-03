from django.shortcuts import render

# Create your views here.

"""This is a  view that displays the index page"""

def all_index(request):

    return render(request, "index.html")
