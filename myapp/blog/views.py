from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
from django.urls import reverse
import logging
from .models import Post, AboutUs
from django.core.paginator import Paginator
from .forms import ContactForm 

#Static data
# posts = [
#         {'id':1, 'title':'Post 1', 'content': 'Content of post 1'},
#         {'id':2,'title':'Post 2', 'content': 'Content of post 2'},
#         {'id':3,'title':'Post 3', 'content': 'Content of post 3'},
#         {'id':4,'title':'Post 4', 'content': 'Content of post 4'},
#     ]

# Create your views here.
def index(request):
    blog_title = "Latest Post"
    #Getting data from post model
    # posts=Post.objects.all()
    #Getting all data

    all_posts = Post.objects.all()
    #Pagination
    paginator  = Paginator(all_posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'blog/index.html',{'blog_title': blog_title, 'page_obj':page_obj})
     
def detail(request, slug):
    #Static data
    #post = next((item for item in posts if item['id'] == int(post_id)), None)
    #logger=logging.getLogger("Testing")
    #logger.debug(f'Post variable is {post}')
    try:
    #Getting data from model by id
        post=Post.objects.get(slug=slug)
        related_posts = Post.objects.filter(category=post.category).exclude(pk=post.id)
        return render(request,'blog/detail.html', {'post':post, 'related_posts': related_posts})
    except Post.DoesNotExist:
        raise Http404("Post not found")

def old_url_redirect(request):
    return redirect(reverse("blog:new_page_url"))

def new_url_view(request):
    return HttpResponse("This is the new URL")

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        logger=logging.getLogger("Testing")
        if form.is_valid():
            logger.debug(f"POST Data is {form.cleaned_data['name']} {form.cleaned_data['message']}")
             # send email code or save in database
            success_message = "Your email has been sent"
            return render(request,'blog/contact.html', {'form':form, 'success_message': success_message})
        else:
            logger.debug("Form validation failure")
        return render(request,'blog/contact.html', {'form':form, 'name':name, 'email':email, 'message':message})
    return render(request,'blog/contact.html')

def about_view(request):
    about_content = AboutUs.objects.first().content
    return render(request,'blog/about.html',{'about_content':about_content})
