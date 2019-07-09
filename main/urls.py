from django.contrib import admin
from django.urls import path
from facebook.views import play
from facebook.views import play2
from facebook.views import profile
from facebook.views import newsfeed
from facebook.views import detail_feed
from facebook.views import pages
from facebook.views import new_feed
from facebook.views import edit_feed
from facebook.views import remove_feed
from facebook.views import fail
from facebook.views import new_page
urlpatterns = [
    path('new_page/', new_page),
    path('admin/', admin.site.urls),
    path('play/', play),
    path('play2/', play2),
    path('leejonghwa/profile/', profile),
    path('', newsfeed),
    path('feed/<pk>/', detail_feed),
    path('pages/', pages),
    path('new/', new_feed),
    path('feed/<pk>/edit/', edit_feed),
    path('feed/<pk>/remove/', remove_feed),
    path('fail/', fail)
]
