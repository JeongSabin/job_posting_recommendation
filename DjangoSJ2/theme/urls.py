from django.contrib import admin
from django.urls import path

import theme
from theme.views import *

app_name = 'theme'

urlpatterns = [
    path('', index, name='index'),
    path('about-us.html', about_us, name='about_us'),
    path('blog-grid-sidebar.html', blog_grid_sidebar, name='blog_grid_sidebar'),
    path('blog-single.html', blog_single, name='blog_single'),
    path('blog-single-sidebar.html', blog_single_sidebar, name='blog_single_sidebar'),
    path('bookmarked-items.html', bookmarked_items, name='bookmarked_items'),
    path('category.html', category, name='category'),
    path('coming-soon.html', coming_soon, name='coming_soon'),
    path('contact.html', contact, name='contact'),
    path('dashboard.html', dashboard, name='dashboard'),
    path('delete-account.html', delete_account, name='delete_account'),
    path('error.html', error, name='error'),
    path('faq.html', faq, name='faq'),
    path('favourite-items.html', favourite_items, name='favourite_items'),
    # path('index2.html', index2, name='index2'),
    # path('index3.html', index3, name='index3'),
    path('invoice.html', invoice, name='invoice'),
    path('item-details.html', item_details, name='item_details'),
    path('item-listing-grid.html', item_listing_grid, name='item_listing_grid'),
    path('item-listing_list.html', item_listing_list, name='item_listing_list'),
    path('login.html', login, name='login'),
    path('mail-success.html', mail_success, name='mail_success'),
    path('my-items.html', my_items, name='my_items'),
    path('messages.html', messages, name='messages'),
    path('post-item.html', post_item, name='post_item'),
    path('pricing.html', pricing, name='pricing'),
    path('profile-settings.html', profile_settings, name='profile_settings'),
    path('registration.html', registration, name='registration'),
]