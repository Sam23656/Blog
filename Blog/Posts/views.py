from django.shortcuts import render, redirect
from Posts.forms import PostAddModelForm
from Posts.models import Post


# Create your views here.


def show_index_page(request):
    context = {"Posts": Post.objects.all()}
    return render(request, "index.html", context=context)


def show_post_page(request, id):
    if request.method == "POST":
        post = Post.objects.get(pk=id)
        post.Likes += 1
        post.save()
    context = {"Post": Post.objects.get(pk=id)}
    return render(request, "post.html", context=context)


def show_add_post_page(request):
    if request.method == "POST":
        form = PostAddModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = PostAddModelForm()

    context = {"form": form}
    return render(request, "addPost.html", context=context)
