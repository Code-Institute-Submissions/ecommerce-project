from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from django.contrib import messages, auth
from django.core.urlresolvers import reverse
from .forms import UserLoginForm, UserRegistrationForm
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from bugs.models import Bugs
from features.models import Features
from cart.models import Cart
from cart.views import cart_items


def index(request):
    """A view that displays the index page"""
    return render(request, "index.html")


@login_required
def logout(request):
    """A view that logs the user out and redirects back to the index page"""
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('index'))


def login(request):
    """A view that manages the login form"""
    if request.method == 'POST':
        user_form = UserLoginForm(request.POST)
        if user_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
            if user:
                auth.login(request, user)
                messages.error(request, "You have successfully logged in")

                Cart.objects.create(user=user).save()
                if request.GET and request.GET['next'] != '':
                    next = request.GET['next']
                    return HttpResponseRedirect(next)
                else:
                    return redirect(reverse('index'))
            else:
                user_form.add_error(
                    None, "Your username or password are incorrect")
    else:
        user_form = UserLoginForm()

    args = {'user_form': user_form, 'next': request.GET.get(
        'next', '')}
    return render(request, 'login.html', args)


@login_required
def profile(request):
    """A view that displays the profile page of a logged in user"""
    Cart.objects.create(user=request.user).save()
    bugs = Bugs.objects.filter(author=request.user)
    features = Features.objects.filter(user=request.user)
    return render(request, 'profile.html', {
        "bugs": bugs, 'features': features, 'profile': True, "len_items": cart_items(request)})


def register(request):
    """A view that manages the registration form"""
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # user_form.save()

            user = User.objects.create_user(
                username=request.POST['username'],
                email=request.POST['email'],
                password=request.POST['password1'])

            user.save()
            Cart.objects.create(user=user).save()
            auth.login(request, user)
            messages.success(request, "You have successfully registered")
            return redirect(reverse('index'))

            # else:
            #     messages.error(request, "unable to log you in at this time!")
    else:
        user_form = UserRegistrationForm()

    args = {'user_form': user_form}
    return render(request, 'register.html', args)


@login_required
def user_profile(request):
    """The user's profile page"""
    userss = User.objects.get(email=request.user.email)
    return render(request, 'profie.html', {"profile": userss})