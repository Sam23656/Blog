from django.shortcuts import render
from Blog.forms import PostAddModelForm
from Posts.models import Post


# Create your views here.


def show_index_page(request):
    context = {"Posts": Post.objects.all()}
    return render(request, "index.html", context=context)


def show_post_page(request, id):
    context = {"Post": Post.objects.get(pk=id)}
    return render(request, "post.html", context=context)


def show_add_post_page(request):
    if request.method == "POST":
        ...
    else:
        form = PostAddModelForm()

    context = {"form": form}
    return render(request, "addPost.html", context=context)
