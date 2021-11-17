from django.urls import path
from .import views


urlpatterns = [
    path('listings/', views.listings, name='listings'),
    path('listings/<int:id>/', views.listing_detail, name='listing_detail'),
    path('search/', views.search, name='search'),


]
