
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from .functions import *

# local imports 
from .forms import ProfileForm, ProfileImageForm
from .models import Profile

# Create your views here.

@login_required
def dashboard(request):

    context = {}
    return render(request, 'dashboard/index.html', context=context)

@login_required
def profile(request):
    context = {}
    profile = request.user


    if request.method == 'GET':
        form  = ProfileForm(instance=request.user.profile, user = request.user)
        image_form = ProfileImageForm(instance=request.user.profile)
        context['form'] = form
        context['image_form'] = image_form

        return render(request, 'dashboard/profile.html', context)

    if request.method == 'POST':
        form  =  ProfileForm(request.POST, instance=request.user.profile)
        image_form = ProfileImageForm(request.POST, request.FILES, instance=request.user.profile)
 

        if form.is_valid():
            form.save()
            return redirect('profile')
        if image_form.is_valid():
            image_form.save()
            return redirect('profile')


    # form = ProfileForm()

    

    
    return render(request, 'dashboard/profile.html', context=context)


def blog_topic_generator(request):
    context = {}

    if request.method == 'POST':
        blog_topic = request.POST['blog_keyword']
        blog_keyword = request.POST['blog_keyword']

        blogTopics = generate_blog_topic(topic=blog_topic, keywords=blog_keyword).replace('\n', '')
        print('Valid')
        print(request.POST['blog_keyword'])

    return render(request, 'dashboard/topic_generator.html', context=context)