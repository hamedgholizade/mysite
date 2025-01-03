from django.shortcuts import render,get_object_or_404,HttpResponseRedirect,reverse
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from blog.models import Post,Comment
from blog.forms import CommentForm
from django.db.models import Q
from django.http import HttpResponse,JsonResponse
from django.contrib import messages

def blog_view(request,**kwargs):
    posts = Post.objects.filter(status=1)
    if kwargs.get('author_name') != None :
        posts = posts.filter(author__username=kwargs['author_name'])
    if kwargs.get('cat_name') != None :
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('tag_name') != None :
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])
    posts = Paginator(posts,3)
    try:
        page_number = request.GET.get("page")
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
       posts = posts.get_page(1)
    except EmptyPage:
       posts = posts.get_page(1)
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)

def single_view(request,pid):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,"Your comment submitted successfully")
        else:
            messages.add_message(request,messages.ERROR,"Your comment did not submit correctly")
    posts = Post.objects.filter(status=1)
    post = get_object_or_404(posts,pk=pid)
    if request.user.is_authenticated:
        comments = Comment.objects.filter(post=post.id,approved=True)
        form = CommentForm()
        context = {"post":post,"comments":comments,"form":form}
        return render(request,("blog/blog-single.html"),context)
    else:
        if not post.login_required:
            comments = Comment.objects.filter(post=post.id,approved=True)
            form = CommentForm()
            context = {"post":post,"comments":comments,"form":form}
            return render(request,("blog/blog-single.html"),context)
        else:
            return HttpResponseRedirect(reverse('accounts:login'))
    
def blog_search(request):
    posts = Post.objects.filter(status=1)
    if request.method == 'GET':
        if s:= request.GET.get("s"):
            posts = posts.filter(Q(content__contains=s)|Q(title__contains=s))
    context = {"posts":posts}
    return render(request,("blog/blog-home.html"),context)

#def blog_category(request,cat_name):
#    posts = Post.objects.filter(status=1)
#    posts.filter(category__name=cat_name)
#    context = {"posts":posts}
#    return render(request,("blog/blog-home.html"),context)

def test_view(request):
    return render(request,("test.html"))