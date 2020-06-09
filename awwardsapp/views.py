from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from .forms import *



@login_required
def PostList(request):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    context = {
        'form':Post_project,
        'post_list': queryset
    }

    return render(request, 'index.html', context )

def PostNew(request):
    data= Post_project(request.POST,request.FILES)
    if data.is_valid():
        new_post = data.save()
        return redirect('profile')
    else:
        return redirect('home')

def logout_view(request):
    logout(request)
    return redirect('home')


def profile(request):
    if request.method == 'GET':
        user_posts = Post.objects.filter(author = request.user.id)
        user_profile = Profile.objects.get(user = request.user)
        # import pdb; pdb.set_trace()


        updateform = UpdateProfile()
        userupdateform = UserProfile()

        context = {
            "user":request.user,
            "posts":user_posts,
            'profile': user_profile,
            'form1': updateform,
            'form2': userupdateform
        }
        return render(request, 'profile.html',context)

    else:
        data = UpdateProfile(request.POST, request.FILES)
        data2 = UserProfile(request.POST)


        if data.is_valid() and data2.is_valid():
            updatedprofile = data.save()
            userprofile = data2.save()

            return redirect('profile')

        else:
            return redirect('profile')
            


