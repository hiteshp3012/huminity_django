from django.urls import path
from . import views

urlpatterns=[
    path('',views.home),
    path('home/',views.home),
    path('ourevents/',views.ourevents),
    path('membership/',views.memberships),
    path('donatenow/',views.donatenow),
    path('gallery/',views.imagegallery),
    path('aboutus/',views.aboutus),
    path('contactus/',views.contactus),
    path('login/',views.login),
    path('videos/',views.videogallery),
    ]