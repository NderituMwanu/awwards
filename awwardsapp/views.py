from django.shortcuts import render
from .models import Post
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.contrib.auth import login, authenticate
# Create your views here.

#@login_required(login_url='/accounts/login/')
class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


#@login_required(login_url='/accounts/login/')
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

# def login(request):
#     if request.method == "POST":
#         form = LoginForm(request.POST)

#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']

#             HttpResponseRedirect('login')
#         else:
#             form = LoginForm()
#         return render(request, '/post_detail.html', )

def logout(request):
    return render(request, '/accounts/login.html')

# def registration(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             user.refresh_from_db()
#             user.profile.birth_date = form.cleaned_data.get('birth_date')
#             user.save()
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(password=raw_password)
#             login(request, user)
#             return redirect('home')
#         else:
#             form = SignUpForm()
#         return render(request, 'registration.html', {'form': form})

