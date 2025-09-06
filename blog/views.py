from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as django_logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import SignUpForm, PostForm, CommentForm
from .models import Post

def home(request):
    posts = Post.objects.all().order_by("-created_at")
    return render(request, "blogs/home.html", {"posts": posts})

def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("login")
        else:
            # Return form with errors and 400 status for invalid form submission
            return render(request, "blogs/signup.html", {"form": form}, status=400)
    else:
        form = SignUpForm()
    return render(request, "blogs/signup.html", {"form": form})

@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("home")
    else:
        form = PostForm()
    return render(request, "blogs/create_post.html", {"form": form})

@login_required
def profile_view(request):
    user_posts = Post.objects.filter(author=request.user).order_by("-created_at")
    try:
        profile = request.user.profile
    except:
        from .models import Profile
        profile = Profile.objects.create(user=request.user)
    return render(request, "blogs/profile.html", {"user_posts": user_posts, "profile": profile})

from django.urls import reverse

from .forms import UserProfileForm

from .forms import ProfileForm

@login_required
def edit_profile(request):
    user = request.user
    try:
        profile = user.profile
    except:
        from .models import Profile
        profile = Profile.objects.create(user=user)

    if request.method == "POST":
        user_form = UserProfileForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("profile")
    else:
        user_form = UserProfileForm(instance=user)
        profile_form = ProfileForm(instance=profile)

    context = {
        "user_form": user_form,
        "profile_form": profile_form,
    }
    return render(request, "blogs/edit_profile.html", context)

@login_required
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # Check if the current user is the author of the post
    if post.author != request.user:
        return redirect("home")  # Or show an error message

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("post_detail", pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, "blogs/edit_post.html", {"form": form, "post": post})

@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # Check if the current user is the author of the post
    if post.author != request.user:
        return redirect("home")  # Or show an error message

    if request.method == "POST":
        post.delete()
        return redirect("home")

    return render(request, "blogs/delete_post.html", {"post": post})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect("post_detail", pk=pk)
    else:
        form = CommentForm()
    return render(request, "blogs/post_detail.html", {"post": post, "comments": comments, "form": form})

def logout_view(request):
    """
    Custom logout view for faster logout process
    """
    if request.method == 'POST':
        # Clear the session data
        request.session.flush()

        # Log the user out using Django's logout
        django_logout(request)

        # Redirect to home page immediately
        return HttpResponseRedirect(reverse('home'))

    # If not POST, redirect to home
    return HttpResponseRedirect(reverse('home'))
