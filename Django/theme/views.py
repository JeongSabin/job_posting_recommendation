from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.utils import json

from .models import *
from django.core.paginator import Paginator
import theme.recommendation_module as rm
from django.db import connection

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

# @method_decorator(csrf_exempt, name='dispatch')
# @csrf_exempt


likes = []

def likeSwitch(request):
    try:
        parms = json.loads(request.body)
        if(parms['like'] == 'on'):
            # 좋아요 등록 처리
            bookmarked_post = bookmark(post_id = parms['pk'])
            bookmarked_post.save()
            likes.append(parms['pk'])
            print(likes)
        elif(parms['like'] == 'off'):
            bookmarked_post = bookmark.objects.get(post_id=parms['pk'])
            bookmarked_post.delete()
            # 좋아요 취소 처리
            likes.remove(parms['pk'])
            print(likes)

        code = 'success'
    except Exception as e:
        code = 'fail'

    return JsonResponse({'code': code})


def about_us(request):
    return render(request, 'about-us.html')

def bookmark_recommendation(request):
    bookmarked = list(bookmark.objects.all())
    bookmarked_post_id_list = list(map(int, bookmarked))
    post_list = post.objects.filter(id__in=bookmarked_post_id_list)
    category_lst = []
    for i in post_list:
        if i.category not in category_lst:
            category_lst.append(i.category)
        else:
            pass
    recommendation_lst = rm.Make_Tfidf_model(category_lst, post_list)
    lst = []
    for i in recommendation_lst:
        lst.append(i)
    data_lst = []
    company_list = []
    cnt = 0
    for i in lst:
        if cnt < 10:
            if post.objects.get(id=i).company not in company_list:
                company_name = ''.join(post.objects.get(id=i).company)
                company_name.replace(' ', '')
                data_lst.append(post.objects.get(id=i))
                company_list.append(company_name)
                cnt += 1
            else:
                pass
        else:
            break

    return render(request, 'bookmark_recommendation.html', {'data_lst': data_lst})



def blog_grid_sidebar(request):
    bookmarked = list(bookmark.objects.all())
    bookmarked_post_id_list = list(map(int, bookmarked))
    post_list = post.objects.filter(id__in=bookmarked_post_id_list)


    return render(request, 'blog-grid-sidebar.html', {'post_list': post_list,
                                                      'bookmarked_post_id_list': bookmarked_post_id_list})

def blog_single(request):
    return render(request, 'blog-single.html')

def blog_single_sidebar(request):
    return render(request, 'blog-single-sidebar.html')

def bookmarked_items(request):
    return render(request, 'bookmarked-items.html')



def category(request, category_name):
    # 디폴트값 웹 개발자, 카테고리 종류별로 리스트 만들어서 html에서 for문으로 출력하기
    category_posts = post.objects.filter(category=category_name)  # 모든 데이터 조회, 내림차순(-표시) 조회
    paginator = Paginator(category_posts, 12)
    page = int(request.GET.get('page', 1))
    posts = paginator.get_page(page)
    category_posts_list = paginator.get_page(page)
    bookmarked = list(bookmark.objects.all())
    bookmarked_post_id_list = list(map(int, bookmarked))
    print(category_posts)


    return render(request, 'category.html', {'category_posts_list': category_posts_list,
                                             'posts': posts,
                                             'bookmarked_post_id_list': bookmarked_post_id_list,})

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
    skill = Post.skill_stack
    skills = list(skill.split())
    category_ = Post.category
    url_ = Post.page_url
    cosine_sim = rm.cosin_sim_calculation(category_, url_)
    recommendation_lst = rm.recommendation_(category_, cosine_sim)
    lst = []
    for i in recommendation_lst:
        lst.append(i)
    data_lst = []
    company_list = []
    cnt = 0
    for i in lst:
        if cnt < 6:
            if post.objects.get(category=category_, id=i).company not in company_list:
                company_name = ''.join(post.objects.get(category=category_, id=i).company)
                company_name.replace(' ', '')
                data_lst.append(post.objects.get(category=category_, id=i))
                company_list.append(company_name)
                cnt += 1
            else:
                pass
        else:
            break
    bookmarked = list(bookmark.objects.all())
    bookmarked_post_id_list = list(map(int, bookmarked))
    return render(request, 'item-details.html', {'Post': Post,
                                                 'data_lst': data_lst,
                                                 'skills': skills,
                                                 'bookmarked_post_id_list': bookmarked_post_id_list})

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

def portfolio(request):
    return render(request, 'faq.html')