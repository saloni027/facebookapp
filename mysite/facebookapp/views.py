
# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from social_django.models import UserSocialAuth

from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from django.contrib.auth import logout



# Create your views here.
def login(request):
    return render(request, 'facebookapp/login.html')


def logout_view(request):
    logout(request)
    return render(request, 'facebookapp/login.html')


@login_required
def home(request):
    return render(request, 'facebookapp/home.html')


def deactivate(request):
    UserSocialAuth.objects.filter(user=request.user).delete()
    User.objects.filter(pk=request.user.pk).update(is_active=False)
    return HttpResponseRedirect(reverse('logout'))
