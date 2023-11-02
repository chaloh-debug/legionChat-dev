from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile
from django.http import HttpResponse

from .forms import CustomUserChangeForm, UpdateProfileForm

class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    
@login_required
def profile(request, *args, **kwargs):
    context = {}

    if request.method == 'POST':
        user_form = CustomUserChangeForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='chat')
    else:
        user_form = CustomUserChangeForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)
    
    context['user_form'] = user_form
    context['profile_form'] = profile_form


    return render(request, 'profile1.html', context)

def account(request, *args, **kwargs):
    context = {}
    user_id = kwargs.get("user_id")
    try:
        account = Profile.objects.get(pk=user_id)
    except Profile.DoesNotExist:
        return HttpResponse("Profile does not exist!")
    
        
    is_self = True
    is_friend = False
    user = request.user.id
    if user != account:
        is_self = False
    elif user == account:
        is_self = True

    context['id'] = account.id
    context['username'] = account.user.username
    context['email'] = account.user.email
    context['avatar'] = account.avatar.url
    context['bio'] = account.bio

    context['is_self'] = is_self
    context['is_friend'] = is_friend

    return render(request, 'account/account.html', context)


def account_search(request):
    context = {}
    if request.method == "GET":
        search_req = request.GET.get("q")
        if len(search_req) > 0:
            search_res = User.objects.filter(email__icontains=search_req).filter(
                username__icontains=search_req).distinct()
            accounts = []
            for account in search_res:
                accounts.append((account, False))
                context['accounts'] = accounts

    return render(request, "account/search_req.html", context)