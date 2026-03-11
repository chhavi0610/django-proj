from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def home(request):
    posts = Post.objects.all()


    return render(request, "home.html", {"posts": posts})

@login_required
def profile(request):

     user = request.user

     return render(request, "profile.html", {"user":user})

def about(request):

    return render(request, "about.html")

def contact(request):

    return render(request, "contact.html")



def signup(request):
     
     if request.method == "POST":
          
          username = request.POST["username"]
          password = request.POST["password"]

          User = get_user_model()
          User.objects.create_user(
               username=username,
               password=password

          )

          return redirect("/login")
     
     return render(request,"signup.html")


def user_login(request):
     
     if request.method == "POST":
          username = request.POST["username"]
          password = request.POST["password"]

          user = authenticate(
               request,
               username = username,
               password= password
          )

          if user is not None:
               login(request, user)
               messages.success(request,"Login successful")
               return redirect('/profile')
          else:
            messages.error(request,"Invalid credentials")

     return render(request, "login.html")
          
def user_logout(request):
     
     logout(request)

     return redirect("/")

@login_required
def create_post(request):

    if request.method == "POST":

        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
           
            return redirect('/')
        
    else:
            form = PostForm()

            return render(request, "create_post.html", {"form":form})
    
@login_required
def edit_post(request, post_id):

     post = get_object_or_404(Post, id = post_id)
     if post.author != request.user:
          return redirect('/')
     
     if request.method == "POST":
          form = PostForm(request.POST, instance=post)

          if form.is_valid():
               form.save()
               return redirect("/")
          
     else:

          form = PostForm(instance=post)

     return render(request, "edit_post.html", {"form": form})

@login_required
def delete_post(request, post_id):

     post = get_object_or_404(Post, id = post_id)

     if post.author != request.user:

          return redirect("/")
     
     if request.method == "POST":
          post.delete()
          messages.warning(request, "Post deleted successfully!")
          return redirect("/")

     return render(request, "delete_post.html", {"post":post})

