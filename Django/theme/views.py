from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator

# Create your views here.

def about_us(request):
    return render(request, 'about-us.html')

def blog_grid_sidebar(request):
    return render(request, 'blog-grid-sidebar.html')

def blog_single(request):
    return render(request, 'blog-single.html')

def blog_single_sidebar(request):
    return render(request, 'blog-single-sidebar.html')

def bookmarked_items(request, post_id):
    return render(request, 'bookmarked-items.html')

def category(request):
    all_develop_manager_data = post.objects.all().order_by("id")  # 모든 데이터 조회, 내림차순(-표시) 조회
    paginator = Paginator(all_develop_manager_data, 12)
    page = int(request.GET.get('page', 1))
    posts = paginator.get_page(page)
    develop_manager_data_list = paginator.get_page(page)
    return render(request, 'category.html', {'develop_manager_data_list': develop_manager_data_list,
                                             'posts':posts})


def coming_soon(request):
    return render(request, 'coming-soon.html')

def contact(request):
    return render(request, 'contact.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def delete_account(request):
    return render(request, 'delete-account.html')

def error(request):
    return render(request, '404.html')

def faq(request):
    return render(request, 'faq.html')

def favourite_items(request):
    return render(request, 'favourite-items.html')

def index(request):
    return render(request, 'index.html')

def index2(request):
    return render(request, 'index2.html')

def index3(request):
    return render(request, 'index3.html')

def invoice(request):
    return render(request, 'invoice.html')

def item_details(request, pk):
    Post = post.objects.get(pk=pk)
    return render(request, 'item-details.html', {'Post':Post})

def item_listing_grid(request):
    return render(request, 'item-listing-grid.html')

def item_listing_list(request):
    return render(request, 'item-listing-list.html')

def login(request):
    return render(request, 'login.html')

def mail_success(request):
    return render(request, 'mail-success.html')

def my_items(request):
    return render(request, 'my-items.html')

def mail_success(request):
    return render(request, 'mail-success.html')

def my_items(request):
    return render(request, 'my-items.html')

def messages(request):
    return render(request, 'messages.html')

def post_item(request):
    return render(request, 'post-item.html')

def pricing(request):
    return render(request, 'pricing.html')

def profile_settings(request):
    return render(request, 'profile-settings.html')

def registration(request):
    return render(request, 'registration.html')