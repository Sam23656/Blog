from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from Posts.forms import PostAddModelForm, UserPasswordResetForm
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


class PostUpdateView(UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["Title", "Text"]
    template_name = "Posts/editPost.html"
    pk_url_kwarg = "id"

    def test_func(self):
        post = get_object_or_404(Post, pk=self.kwargs[self.pk_url_kwarg])
        is_admin = self.request.user.is_superuser
        is_author = (self.request.user == post.Author)
        return is_admin or is_author

    def handle_no_permission(self):
        return redirect("index")


class PostDeleteView(UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "Posts/deletePost.html"
    success_url = reverse_lazy("index")
    pk_url_kwarg = "id"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["PostPk"] = self.kwargs[self.pk_url_kwarg]
        return context

    def test_func(self):
        post = get_object_or_404(Post, pk=self.kwargs[self.pk_url_kwarg])
        is_admin = self.request.user.is_superuser
        is_author = (self.request.user == post.Author)
        return is_admin or is_author

    def handle_no_permission(self):
        return redirect("index")


class PasswordChangeViewPage(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy("index")
    template_name = "Posts/passwordChange.html"


def password_reset_page(request):
    if request.method == "POST":
        form = UserPasswordResetForm(request.POST)
        user_to_change = get_object_or_404(User, username=form['Name'].value())
        if form.is_valid():
            if form['Name'].value() == user_to_change.username:
                user_to_change.set_password(form['New_Password'].value())
                user_to_change.save()
                return redirect("index")
    else:
        form = UserPasswordResetForm()

    context = {"form": form}
    return render(request, "Posts/passwordReset.html", context=context)
