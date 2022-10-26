"""merchex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from listings import views

urlpatterns = [
    path('', views.band_list, name='band_list'),
    path('admin/', admin.site.urls),
    path('bands/', views.band_list, name = 'band-list'),
    path('bands/<int:id>/', views.band_detail, name='band-detail'),
    path('bands/add', views.band_create, name='band-create'),
    path('bands/<int:id>/edit', views.band_update, name='band-edit'),
    path('bands/<int:id>/delete', views.band_delete, name='band-delete'),
    path('about-us/', views.about),
    path('listings/', views.listings, name='listing-list'),
    path('listings/<int:id>/', views.listing_detail, name='listing-detail'),
    path('listings/add', views.listing_create, name='listing-create'),
    path('listing/<int:id>/edit', views.listing_update, name='listing-edit'),
    path('listing/<int:id>/delete', views.listing_delete, name='listing-delete'),
    path('contact/', views.contact, name='contact'),
    path('about', views.about, name='about'),
    
]

