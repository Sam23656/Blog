from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from Posts.forms import PostAddModelForm
from Posts.models import Post


# Create your views here.


def show_index_page(request):
    context = {"Posts": Post.objects.all()}
    return render(request, "Posts/index.html", context=context)


def show_post_page(request, id):
    if request.method == "POST":
        post = Post.objects.get(pk=id)
        post.Likes += 1
        post.save()
    context = {"Post": Post.objects.get(pk=id)}
    return render(request, "Posts/post.html", context=context)


@login_required
def show_add_post_page(request):
    if request.method == "POST":
        form = PostAddModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = PostAddModelForm()

    context = {"form": form}
    return render(request, "Posts/addPost.html", context=context)


class LogoutViewPage(LogoutView):
    next_page = reverse_lazy("index")


class LoginViewPage(LoginView):
    template_name = "Posts/login.html"
    form_class = AuthenticationForm
    next_page = reverse_lazy("index")


class RegisterViewPage(CreateView):
    template_name = "Posts/register.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("index")
