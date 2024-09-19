from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
import logging
from .models import Post, AboutUS
from django.http import Http404
from django.core.paginator import Paginator
from .forms import ContactForm

# Create your views here.
#static demo data...
# posts =[
#         {'id':1,'title': 'post 1','content': "content of post 1"},
#         {'id':2,'title': 'post 2','content': "content of post 2"},
#         {'id':3,'title': 'post 3','content': "content of post 3"},
#         {'id':4,'title': 'post 4','content': "content of post 4"}
#      ]


def index(request):
    blog_title  ="MK Latest Posts"
    
    #getting data from post model
    all_posts = Post.objects.all()

    #paginate
    paginator = Paginator(all_posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    return render(request,'blog/index.html', {'blog_title': blog_title, 'page_obj': page_obj})

def detail(request, post_id):
    # Static data
    #post = next((item for item in posts if item['id'] == int(post_id)), None)

    try:
        #getting Data From model bt post id
        post =Post.objects.get(pk=post_id)
        related_posts =Post.objects.filter(category = post.category).exclude(pk=post.id)
    except Post.DoesNotExist:
        raise Http404("Post Dose not exist")


    # logger = logging.getLogger("TESTING")
    # logger.debug(f'post variable is {post}')
    return render(request,'blog/detail.html', {'post': post, 'related_posts': related_posts})

def old_url_redirect(request):
    return redirect(reverse('blog:new_url'))

def new_url_view(request):
    return HttpResponse("This is the new URL")

def contact_v(request):
    form = ContactForm(request.POST)
    name = request.POST.get('name')
    email = request.POST.get('email')
    message = request.POST.get('message')

    logger = logging.getLogger("TESTING")
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            logger.debug(f'POST Data is {form.cleaned_data['name']} {form.cleaned_data['email']} {form.cleaned_data['message']}')
            success_message = 'Your Email has been sent!'
            #send email in database
            return render(request,'blog/contact.html', {'form':form,'success_message':success_message})
        else:
            logger = logging.getLogger("Form validitation Failure")
        return render(request,'blog/contact.html', {'form':form, 'name': name, 'email':email, 'message': message})

    return render(request,'blog/contact.html')

def about(request):
    about_content = AboutUS.objects.first().contents
    return render(request, 'blog/about.html',{'about_content':about_content})
