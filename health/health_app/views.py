#from django.shortcuts import render
from django.http import HttpResponse
from .models import Board, Customer, Post

from .forms import *
from django.views import generic

from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate,login as dj_login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template import RequestContext


# Create your views here.
def home(request):
    boards = Board.objects.all()
    return render(request, 'index.html',{"boards" : boards})

def board_search(request):
    boards = Board.objects.filter(title_post__contains = request.GET['board_search'])
    return render(request,'index.html',{"boards": boards})


def lifestyle(request):
    return render(request, 'lifestyle.html')

def food(request):
    return render(request, 'food.html')

def health(request):
    return render(request, 'health.html')

def beauty(request):
    return render(request, 'beauty.html')

def video(request):
    return render(request, 'video.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def create_post(request):
    if request.method == 'POST':
        context = RequestContext(request)
        return redirect('home')

    return render(request, 'create_post.html')

def register(request):
    
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            context = RequestContext(request)
            form.save()
            user = form.save()
            login(request, user)
            return redirect('posts:list',context)
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
 

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "post_page.html"
    paginate_by = 3


def post_detail(request, slug):
    
    template_name = "post_detail.html"
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True).order_by("-created_on")
    new_comment = None
    # Comment posted
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(
        request,
        template_name,
        {
            "post": post,
            "comments": comments,
            "new_comment": new_comment,
            "comment_form": comment_form,
        },
    )

def login(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				dj_login(request, user)
				return redirect('home')
                
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'login.html', context)

