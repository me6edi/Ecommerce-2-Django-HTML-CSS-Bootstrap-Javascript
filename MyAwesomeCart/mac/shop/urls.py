
from django.urls import path
from . import views
urlpatterns = [
path('', views.index, name="ShopHome"),
path('about/', views.about, name="aboutUs"),
path('contact/', views.contact, name="contactUs"),
path('tracker/', views.tracker, name="TrackingStatus"),
path('search/', views.search, name="Search"),
path('productview/', views.productView, name="Productview"),
path('checkout/', views.checkout, name="Checkout"),
] 