from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from posts.forms import PostEditForm, ContactForm, PostCreateForm
from posts.models import Post


# Create your views here.

def posts_list(request):
    if request.method == "POST":
        form = PostCreateForm(data=request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            # post = Post(**form.cleaned_data)
            # post.author = request.user
            # post.save()
            instance.author = request.user
            instance.save()

    form = PostCreateForm()
    num_page = request.GET.get("page", 1)
    per_page = request.GET.get("per_page", 25)

    posts = Post.objects.all()

    p = Paginator(posts, per_page)
    page_obj = p.page(num_page)

    return render(
        request,
        "posts/list.html",
        {
            "page_obj": page_obj,
            "form": form

        }
    )


def post_details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = PostCreateForm(instance=post)

    if request.method == "POST":
        form = PostCreateForm(data=request.POST, instance=post)

        # title = request.POST.get("title")
        #
        # post.title = title
        # post.save()
        if form.is_valid():
            form.save()

    return render(
        request,
        "posts/details.html",
        {
            "post": post,
            "form": form
        }
    )


def contact(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(data=request.POST)
        if form.is_valid():
            print("Contact poprawny")
        else:
            print("Contact niepoprawny")
            print(form.errors)

    return render(request, "posts/contact.html", {"form": form})
